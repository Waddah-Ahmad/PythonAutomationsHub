
# Project: Automated AWS Lambda Function Deployment
"""
Description: This project automates the process of deploying an AWS Lambda function using Boto3.
It allows you to package your Python function code, upload it to AWS Lambda, and configure the necessary settings.

Steps:

Install Boto3 and configure AWS credentials (access key and secret key) on your machine.
Write a Python script that uses Boto3 to interact with AWS Lambda API.
Define the Python function code that you want to deploy as an AWS Lambda function.
Package the function code along with its dependencies into a ZIP file.
Use Boto3 to create or update the AWS Lambda function with the packaged code.
Requirements:

Python with Boto3 installed (can be installed using pip install boto3).
AWS account and credentials (access key and secret key) configured on your machine.
"""

import boto3
import zipfile
import os

def create_lambda_function(func_name, role_arn, runtime, handler, zip_file_path):
    with open(zip_file_path, 'rb') as zip_file:
        zip_content = zip_file.read()

    lambda_client = boto3.client('lambda')
    response = lambda_client.create_function(
        FunctionName=func_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={
            'ZipFile': zip_content
        }
    )

    return response['FunctionArn']

if __name__ == "__main__":
    function_name = "MyLambdaFunction"
    role_arn = "arn:aws:iam::<<accountID>>:role/my-lambda-role"  # Replace with your IAM role ARN
    runtime = "python3.8"
    handler = "lambda_function.handler"  # Replace with your Python function's handler
    zip_file_path = "lambda_function.zip"  # Replace with the path to your function's ZIP file

    # Package the function code and its dependencies into a ZIP file
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        zip_file.write("lambda_function.py")  # Replace with the path to your Python function code
        # Include any additional dependencies (e.g., external libraries)

    function_arn = create_lambda_function(function_name, role_arn, runtime, handler, zip_file_path)
    print(f"AWS Lambda function {function_name} created with ARN: {function_arn}")