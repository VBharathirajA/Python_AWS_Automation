Python AWS Automation (S3 & EC2)
Project Overview

This project is a Python-based AWS automation tool that performs common cloud operations using the Boto3 SDK. It allows users to manage S3 buckets and EC2 instances through a command-line interface.

The goal of this project is to demonstrate AWS automation using Python, including storage management and compute instance provisioning.

Technologies Used

Python 3

Boto3 (AWS SDK for Python)

Amazon S3

Amazon EC2

AWS CLI

JSON

Python Exception Handling

Features
S3 Operations

The project automates common S3 tasks such as:

Create S3 bucket

List all buckets

Upload files to bucket

Download files from bucket

List objects in bucket

Delete objects

Delete bucket

Check if bucket exists

EC2 Operations

The automation tool can manage EC2 instances:

Launch EC2 instance

View instance details

Manage instance lifecycle

Project Structure
aws-python-automation
│
├── main.py
├── s3_operations.py
├── ec2_operations.py
├── config.py
└── README.md
Installation
1 Install Python

Install Python 3.x from the official website.

2 Install Boto3
pip install boto3
3 Configure AWS Credentials

Use AWS CLI:

aws configure

Provide:

AWS Access Key
AWS Secret Key
Region
Output format
How to Run the Project

Run the main program:

python main.py

Example menu:

1 EC2 Operations
2 S3 Operations
3 Exit
Example S3 Operation (Upload File)
import boto3

s3 = boto3.client('s3')

s3.upload_file(
    'test.txt',
    'my-bucket-name',
    'test.txt'
)
Example EC2 Instance Creation
import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-xxxxxxxx',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)
Learning Objectives

This project helps practice:

AWS cloud automation

Python scripting for infrastructure

Boto3 client and resource methods

Exception handling

Cloud resource management

Future Improvements

Add IAM automation

Add S3 presigned URLs

Add EC2 start/stop automation

Logging system

Web interface using Flask

Author

Bharathi V

Python & AWS Cloud Learner
Focused on cloud automation and DevOps practices.
