import os
import shutil
import random

# Define paths
dataset_path = "D:/dataset"
images_path = os.path.join(dataset_path, "images")
labels_path = os.path.join(dataset_path, "labels")


# Create output directories
output_dirs = {
    "train": ["train/images", "train/labels"],
    "val": ["val/images", "val/labels"],
    "test": ["test/images", "test/labels"]
}

for key, dirs in output_dirs.items():
    for dir in dirs:
        os.makedirs(os.path.join(dataset_path, dir), exist_ok=True)

# Get all image files
image_files = [f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png'))]

# Shuffle and split dataset
random.shuffle(image_files)
train_split = int(0.8 * len(image_files))
val_split = int(0.9 * len(image_files))

train_files = image_files[:train_split]
val_files = image_files[train_split:val_split]
test_files = image_files[val_split:]

# Function to move files
def move_files(file_list, subset):
    for file in file_list:
        image_src = os.path.join(images_path, file)
        label_src = os.path.join(labels_path, file.replace('.jpg', '.txt'))  # Assuming .jpg images

        if os.path.exists(label_src):  # Move only if corresponding label exists
            shutil.move(image_src, os.path.join(dataset_path, subset, "images", file))
            shutil.move(label_src, os.path.join(dataset_path, subset, "labels", file.replace('.jpg', '.txt')))

# Move files to respective directories
move_files(train_files, "train")
move_files(val_files, "val")
move_files(test_files, "test")

print("Dataset successfully split into train, val, and test sets!")
