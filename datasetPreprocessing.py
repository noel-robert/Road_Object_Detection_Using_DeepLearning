import os
import json
import time
import shutil
from tqdm import tqdm
from lxml import etree
from pathlib import Path



def convert_xml_to_yolo(xml_file, xml_path, class_mapping, output_folder):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    size_element = root.find('size')
    image_width = int(size_element.find('width').text)
    image_height = int(size_element.find('height').text)

    yolo_annotations = []
    for obj in root.findall('object'):
        class_name = obj.find('name').text

        if class_name not in class_mapping:
            class_mapping[class_name] = len(class_mapping)
        class_index = class_mapping[class_name]

        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        x = (xmin + xmax) / (2.0 * image_width)
        y = (ymin + ymax) / (2.0 * image_height)
        w = (xmax - xmin) / image_width
        h = (ymax - ymin) / image_height

        yolo_annotation = f"{class_index} {x:.6f} {y:.6f} {w:.6f} {h:.6f}"
        yolo_annotations.append(yolo_annotation)

    label_filename = xml_path.replace('/', '_') + '.txt'
    output_file = Path(output_folder, label_filename)
    with output_file.open('w') as f:
        f.write('\n'.join(yolo_annotations))


def copy_files(source_file, dest_image_folder, dest_label_folder):
    with open(source_file, 'r') as file:
        lines = file.readlines()

    os.makedirs(dest_image_folder, exist_ok=True)
    os.makedirs(dest_label_folder, exist_ok=True)

    for line in lines:
        line = line.strip()
        image_file = os.path.join('IDD_Detection', 'JPEGImages', line + '.jpg')
        # label_file = os.path.join('IDD_Detection', 'Annotations', line + '.xml')

        image_filename = line.replace('/', '_') + '.jpg'
        # label_filename = line.replace('/', '_') + '.txt'

        dest_image_path = os.path.join(dest_image_folder, image_filename)
        # dest_label_path = os.path.join(dest_label_folder, label_filename)

        try:
            shutil.copy(image_file, dest_image_path)
            print(f"Copied image file: {image_file} to {dest_image_path}")
        except FileNotFoundError:
            print(f"Image file not found: {image_file}")


def convert_dataset(xml_path_files):
    class_mapping = {}
    output_dir = Path('modified_dataset')

    pbar_total = sum(len(open(file).readlines()) for file in xml_path_files)
    pbar = tqdm(total = pbar_total, desc = 'Converting XML to YOLO')

    for xml_path_file in xml_path_files:
        with open(xml_path_file, 'r') as file:
            xml_paths = file.read().splitlines()

        # this is to create test, train and val folders inside labels folder
        new_folder = Path(xml_path_file).stem.split('.')[0]
        output_folder = output_dir / 'labels' / new_folder
        output_folder.mkdir(parents=True, exist_ok=True)
        
        # test folder does not have annotations stored by default, and assuming it is chacked at last only
        if new_folder == 'test': break  
        
        for xml_path in xml_paths:
            folder, subfolder, filename = xml_path.split("/")
            xml_file = Path('IDD_Detection/Annotations') / folder / subfolder / (filename + '.xml')

            convert_xml_to_yolo(xml_file, xml_path, class_mapping, output_folder)
            pbar.update(1)

    pbar.close()

    class_mapping_file = output_dir / 'class_mapping.json'
    with class_mapping_file.open('w') as f:
        json.dump(class_mapping, f)
        

def main():
    xml_path_files = ['IDD_Detection/train.txt', 'IDD_Detection/val.txt', 'IDD_Detection/test.txt']     # test.txt should be at last compulsorily

    start_time = time.time()
    
    # create main directory to store modified dataset
    output_dir = Path('modified_dataset')
    if output_dir.exists() and output_dir.is_dir():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    convert_dataset(xml_path_files)

    dest_train_image_folder = 'modified_dataset/images/train'
    dest_train_label_folder = 'modified_dataset/labels/train'
    dest_val_image_folder = 'modified_dataset/images/val'
    dest_val_label_folder = 'modified_dataset/labels/val'
    dest_test_image_folder = 'modified_dataset/images/test'
    dest_test_label_folder = 'modified_dataset/labels/test'

    copy_files(xml_path_files[0], dest_train_image_folder, dest_train_label_folder)
    copy_files(xml_path_files[1], dest_val_image_folder, dest_val_label_folder)
    copy_files(xml_path_files[2], dest_test_image_folder, dest_test_label_folder)
    
    # pbar_copy = tqdm(total = 3, desc = 'Copying Files')
    
    # pbar_copy.set_description('Copying train files')
    # copy_files(xml_path_files[0], dest_train_image_folder, dest_train_label_folder)
    # pbar_copy.update(1)
    
    # pbar_copy.set_description('Copying val files')
    # copy_files(xml_path_files[1], dest_val_image_folder, dest_val_label_folder)
    # pbar_copy.update(1)
    
    # pbar_copy.set_description('Copying test files')
    # copy_files(xml_path_files[2], dest_test_image_folder, dest_test_label_folder)
    # pbar_copy.update(1)
    
    # pbar_copy.close()


    end_time = time.time()
    execution_time = end_time - start_time

    print("Execution completed in {:.5f} seconds.".format(execution_time))


if __name__ == '__main__':
    main()