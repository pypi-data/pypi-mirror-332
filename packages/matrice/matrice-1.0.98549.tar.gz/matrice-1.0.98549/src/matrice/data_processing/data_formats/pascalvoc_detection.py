import os
import xml.etree.ElementTree as ET
import logging
from matrice.data_processing.server_utils import generate_short_uuid

def calculate_pascal_bbox_properties(bbox):
    if len(bbox) != 4:
        raise ValueError("Bounding box must be in the format [x_min, y_min, x_max, y_max].")
    
    x_min, y_min, x_max, y_max = bbox
    
    # Convert from Pascal VOC to MSCOCO format
    width = x_max - x_min
    height = y_max - y_min

    center_x = x_min + width / 2
    center_y = y_min + height / 2
    
    area = width * height
    
    return {
        "bbox": [float(x_min), float(y_min), float(width), float(height)],
        "height": float(height),
        "width": float(width),
        "center": [float(center_x), float(center_y)],
        "area": float(area)
    }


def get_pascalvoc_image_details(annotation_files):
    """Process Pascal VOC annotation files and extract image details.

    Args:
        annotation_files: List of paths to Pascal VOC annotation files (XML and TXT)

    Returns:
        Tuple containing:
        - Dictionary of image details indexed by file location
        - List of image filenames missing annotations
        - Dictionary of class-wise splits
    """
    complete_images = {}
    missing_annotations = []
    missing_dimensions = {}
    classwise_splits = {}

    logging.info(f"Processing {len(annotation_files)} annotation files")

    if not annotation_files:
        logging.warning("No annotation files provided")
        return complete_images, missing_annotations, classwise_splits

    # Separate XML and TXT files
    xml_files = [f for f in annotation_files if f.lower().endswith('.xml')]
    # Filter TXT files to include only those in ImageSets/Main
    txt_files = [
        f for f in annotation_files
        if f.lower().endswith('.txt') and "ImageSets/Main" in f.replace("\\", "/")
    ]

    logging.debug(f"Processing {len(xml_files)} XML files: {xml_files}")
    logging.debug(f"Processing {len(txt_files)} TXT files: {txt_files}")
    # Process TXT files to determine dataset splits
    split_mapping = {}
    for txt_file in txt_files:
        split_type = os.path.splitext(os.path.basename(txt_file))[0]
        if split_type in ['train', 'val', 'test']:
            if not os.path.exists(txt_file):
                logging.error(f"File not found: {txt_file}")
                continue

            with open(txt_file, 'r') as f:
                for line in f:
                    image_name = line.strip()
                    split_mapping[image_name] = split_type

    
    logging.info(f"Processing {len(xml_files)} XML files to extract annotations")
    for xml_file in xml_files:
        if not os.path.exists(xml_file):
            logging.error(f"File not found: {xml_file}")
            continue

        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            filename = root.find('filename').text
            filename_without_extension = os.path.splitext(filename)[0]
            split_type = split_mapping.get(filename_without_extension, 'unassigned')

            size = root.find('size')
            try:
                width = int(size.find('width').text)
                height = int(size.find('height').text)
            except (TypeError, ValueError):
                missing_dimensions[filename] = {'file_name': filename, 'splitType': split_type}
                width, height = None, None

            annotations = []
            for obj in root.findall('object'):
                category = obj.find('name').text
                bndbox = obj.find('bndbox')
                bbox = [
                    float(bndbox.find('xmin').text),
                    float(bndbox.find('ymin').text),
                    float(bndbox.find('xmax').text),
                    float(bndbox.find('ymax').text)
                ]
                bbox_properties = calculate_pascal_bbox_properties(bbox)

                annotation_json = {
                    "id": str(generate_short_uuid()),
                    "segmentation": [],
                    "isCrowd": [],
                    "confidence": 0.0,
                    "bbox": bbox_properties["bbox"],
                    "height": bbox_properties["height"],
                    "width": bbox_properties["width"],
                    "center": bbox_properties["center"],
                    "area": bbox_properties["area"],
                    "category": str(category),
                    "masks": [],
                }
                annotations.append(annotation_json)

                if category not in classwise_splits:
                    classwise_splits[category] = {"train": 0, "val": 0, "test": 0, "unassigned": 0}
                classwise_splits[category][split_type] += 1

            key = f"{filename}"
            details = {
                "splitType": split_type,
                "file_name": filename,
                "image_height": height,
                "image_width": width,
                "image_area": width * height if width and height else None,
                "annotations": annotations,
            }

            if annotations:
                complete_images[key] = details
            else:
                missing_annotations.append(filename)

        except ET.ParseError as e:
            logging.error(f"Error parsing XML {xml_file}: {e}")
        except Exception as e:
            logging.error(f"Error processing file {xml_file}: {e}")

    logging.info("\nFinal summary:")
    logging.info(f"Complete images: {len(complete_images)}")
    logging.info(f"Missing annotations: {len(missing_annotations)}")
    logging.info(f"Missing dimensions: {len(missing_dimensions)}")

    for category, counts in classwise_splits.items():
        counts['total'] = sum(counts.values())

    return {**complete_images, **missing_dimensions}, missing_annotations, classwise_splits  


def add_pascalvoc_dataset_items_details(batch_dataset_items, images_details):
    processed_batch = []
    for dataset_item in batch_dataset_items:
        image_key = f"{dataset_item.get('filename')}"
        if image_key not in images_details:
            logging.warning(f"'{image_key}' not found in images_details")
            continue
        dataset_item.update(images_details[image_key])
        processed_batch.append(
            {
                "sample_details": dataset_item,
                "is_complete": all(
                    dataset_item.get(k) is not None
                    for k in ["image_height", "image_width"]
                ),
            }
        )
    return processed_batch