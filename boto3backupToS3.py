
# Project: Automated AWS S3 Bucket Backup
"""
Description: This project automates the process of backing up files from a local directory to an AWS S3 bucket using Boto3.
It allows you to easily create backups of your local files to a secure cloud storage solution.

Steps:

Install Boto3 and configure AWS credentials (access key and secret key) on your machine.
Write a Python script that uses Boto3 to interact with AWS S3 API.
Define the local directory to be backed up and the AWS S3 bucket to store the backups.
Use Boto3 to upload the files from the local directory to the AWS S3 bucket.
Requirements:

Python with Boto3 installed (can be installed using pip install boto3).
AWS account and credentials (access key and secret key) configured on your machine.
An existing AWS S3 bucket for storing backups.
"""

import boto3
import os

def upload_to_s3(local_directory, bucket_name):
    s3 = boto3.client('s3')

    for root, dirs, files in os.walk(local_directory):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(bucket_name, relative_path)

            s3.upload_file(local_path, bucket_name, s3_path)
            print(f"Uploaded {local_path} to S3 bucket {bucket_name} with key: {s3_path}")

if __name__ == "__main__":
    local_directory = "/path/to/your/local/directory"  # Replace with the local directory to be backed up
    bucket_name = "your-aws-s3-bucket-name"  # Replace with the name of your existing S3 bucket

    upload_to_s3(local_directory, bucket_name)
    print("Backup completed.")