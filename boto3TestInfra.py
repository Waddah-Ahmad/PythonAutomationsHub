
# Project: Automated AWS Infrastructure Testing
"""
Description: This project automates the process of testing the infrastructure in an AWS environment.
It uses Boto3 to run tests against various AWS resources like EC2 instances,
RDS databases, and S3 buckets to ensure they are configured correctly and functioning as expected.

Steps:

Install Boto3 and configure AWS credentials (access key and secret key) on your machine.
Write a Python script that uses Boto3 to interact with AWS resources for testing.
Define tests for different resources, such as checking if EC2 instances are running or if S3 buckets are accessible.
Run the tests and generate a report of the test results.
Requirements:

Python with Boto3 installed (can be installed using pip install boto3).
AWS account and credentials (access key and secret key) configured on your machine.

"""

import boto3

def test_ec2_instances():
    ec2 = boto3.resource('ec2')
    running_instances = list(ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]))

    if len(running_instances) > 0:
        print("EC2 Instances are running.")
    else:
        print("No running EC2 Instances found.")

def test_rds_databases():
    rds = boto3.client('rds')
    databases = rds.describe_db_instances()

    if 'DBInstances' in databases and len(databases['DBInstances']) > 0:
        print("RDS Databases are running.")
    else:
        print("No running RDS Databases found.")

def test_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    if 'Buckets' in buckets and len(buckets['Buckets']) > 0:
        print("S3 Buckets are accessible.")
    else:
        print("No accessible S3 Buckets found.")

if __name__ == "__main__":
    # Ensure that you have configured your AWS credentials using `aws configure`.

    print("Running AWS Infrastructure Tests...")
    test_ec2_instances()
    test_rds_databases()
    test_s3_buckets()
    print("Infrastructure tests completed.")