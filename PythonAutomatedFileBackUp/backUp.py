
import os
import shutil
import datetime

import schedule
import time

src_dir = "/Users/kunalshenoy/Documents/Screenshots"
destination_dir = "/Users/kunalshenoy/Desktop/BackUps"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    des_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, des_dir)
        print(f"Folder copied to {des_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}")

"""
def l():
    copy_folder_to_directory(src_dir, destination_dir)
    instead use lambda functions to have better code readability
"""

# automation process
# schedule a date and time to automatically back up from one folder to another
schedule.every().day.at("10:10").do(lambda: copy_folder_to_directory(src_dir, destination_dir)) # in line or an anonymous function

while True:
    schedule.run_pending()
    time.sleep(60)
#copy_folder_to_directory(src_dir, destination_dir)