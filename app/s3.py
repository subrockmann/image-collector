import boto3
import botocore
import pandas as pd
import os
from os.path import dirname

CREDENTIALS_FOLDER = os.path.join(dirname(os.path.realpath(__file__)), 'credentials')
print(CREDENTIALS_FOLDER)
CREDENTIALS_FILE = os.path.join(CREDENTIALS_FOLDER,'data-collector-credentials.csv' )
print(CREDENTIALS_FILE)

# access AWS credentials
AWS_KEY_ID = pd.read_csv(CREDENTIALS_FILE)['Access key ID'][0]
AWS_SECRET = pd.read_csv(CREDENTIALS_FILE)['Secret access key'][0]

# define your preferred region
MY_REGION = 'eu-central-1'
BUCKET_NAME = 'data-collector-v1'

def setup_s3():
    # Generate the boto3 client for interacting with S3 and SNS
    s3 = boto3.client('s3',  region_name= MY_REGION,   
        aws_access_key_id=AWS_KEY_ID, 
        aws_secret_access_key=AWS_SECRET)
    return s3

