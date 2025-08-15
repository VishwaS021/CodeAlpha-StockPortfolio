import os
import shutil

source_folder = r"C:\Users\vk256"
destination_folder = r"C:\Users\vk256\JPG images" 

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

moved_count = 0
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        moved_count += 1

print(f" {moved_count} .jpg file(s) moved to {destination_folder}")

