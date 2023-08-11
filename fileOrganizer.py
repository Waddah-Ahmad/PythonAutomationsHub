# Project: File Organizer

# Description: This project automates the organization of files in a specified directory. It identifies different types of files based on their extensions and moves them into respective folders.

# Steps:

# Choose a directory to be organized (e.g., Downloads folder).
# Create folders for different file types (e.g., Documents, Images, Videos, etc.).
# Write a Python script that scans the chosen directory and categorizes files based on their extensions.
# Move each file to the appropriate folder according to its type.
# Run the script to organize the files automatically.

import os
import shutil

def organize_files(source_directory, destination_directory):
    file_extensions = {
        'Documents': ['.txt', '.doc', '.pdf'],
        'Images': ['.jpg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Others': []  # Add any other file extensions to be moved to this folder
    }

    for filename in os.listdir(source_directory):
        file_extension = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_extensions.items():
            if file_extension in extensions:
                source_path = os.path.join(source_directory, filename)
                destination_path = os.path.join(destination_directory, folder)

                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {folder} folder.")

if __name__ == "__main__":
    source_directory = "path/to/your/source/directory"  # Replace with your source directory
    destination_directory = "path/to/your/destination/directory"  # Replace with your destination directory

    organize_files(source_directory, destination_directory)