# Subtask 2.1 - Parse JSON and upload images/files into S3. Return S3 URI once uploaded.

import boto3
from file_crawler import

s3 = boto3.client('s3')

