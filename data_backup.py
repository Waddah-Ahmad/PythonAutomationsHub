
# Project: Automated Data Backup

# Description: This project automates the process of backing up critical data from one directory to another. It allows you to schedule automatic backups at specified intervals and maintains a version history of the backed-up files.


import os
import shutil
import time
from datetime import datetime

def perform_backup(source_dir, destination_dir):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder = os.path.join(destination_dir, f"backup_{timestamp}")

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    for root, _, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(backup_folder, os.path.relpath(source_path, source_dir))

            if not os.path.exists(os.path.dirname(dest_path)):
                os.makedirs(os.path.dirname(dest_path))

            if not os.path.exists(dest_path) or os.stat(source_path).st_mtime > os.stat(dest_path).st_mtime:
                shutil.copy2(source_path, dest_path)
                print(f"Copied {source_path} to {dest_path}")

if __name__ == "__main__":
    source_directory = "path/to/your/source/directory"  # Replace with your source directory
    destination_directory = "path/to/your/destination/directory"  # Replace with your destination directory

    while True:
        perform_backup(source_directory, destination_directory)
        print("Backup completed.")
        time.sleep(3600)  # Schedule the backup to run every hour (3600 seconds)
