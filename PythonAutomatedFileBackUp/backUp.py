
import os
import shutil
import datetime

import schedule
import time

src_dir = "/Users/kunalshenoy/Documents/Obsidian"
destination_dir = "/Users/kunalshenoy/Desktop/BackUps"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    des_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to {des_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}")

copy_folder_to_directory(src_dir, destination_dir)