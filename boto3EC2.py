
# Project: Automated AWS EC2 Instance Deployment

"""
Description: This project automates the process of deploying an AWS EC2 instance using Boto3. It allows you to create an EC2 instance with specified configurations, such as instance type, security groups, and key pair, all through a Python script.

Steps:

Install Boto3 and configure AWS credentials (access key and secret key) on your machine.
Write a Python script that uses Boto3 to interact with AWS EC2 API.
Define the configuration for the EC2 instance, including instance type, security groups, key pair, etc.
Use Boto3 to create the EC2 instance based on the specified configuration.
Requirements:

Python with Boto3 installed (can be installed using pip install boto3).
AWS account and credentials (access key and secret key) configured on your machine.
"""

import boto3

def create_ec2_instance(instance_name, instance_type, security_groups, key_pair_name):
    ec2 = boto3.resource('ec2')

    # Create EC2 instance
    instance = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',  # Replace with the desired AMI ID for your region
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_pair_name,
        SecurityGroups=security_groups,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]
    )

    return instance[0].id

if __name__ == "__main__":
    instance_name = "MyEC2Instance"
    instance_type = "t2.micro"
    security_groups = ["default"]  # Replace with a list of security group names
    key_pair_name = "my-key-pair"  # Replace with the name of your existing key pair

    instance_id = create_ec2_instance(instance_name, instance_type, security_groups, key_pair_name)
    print(f"EC2 instance {instance_name} created with ID: {instance_id}")