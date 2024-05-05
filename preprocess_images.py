import os
import cv2
import numpy as np

def load_images_from_folders(root_dir):
    all_images = []
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                img_path = os.path.join(folder_path, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    img = cv2.resize(img, (224, 224))  # Resize images
                    img = img / 255.0  # Normalize images
                    all_images.append(img)
    return np.array(all_images)


root_dir = 'Face_recognition/data/imdb_dataset/wiki_crop'
images = load_images_from_folders(root_dir)
