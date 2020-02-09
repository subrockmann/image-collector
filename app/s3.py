import boto3
import botocore
from botocore.exceptions import ClientError

import logging
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

s3_resource = boto3.resource('s3')

def setup_s3():
    # Generate the boto3 client for interacting with S3 and SNS
    s3 = boto3.client('s3',  region_name= MY_REGION,   
        aws_access_key_id=AWS_KEY_ID, 
        aws_secret_access_key=AWS_SECRET)
    return s3

def create_bucket_if_not_exists(bucket_name):    
    exists = True
    try:
        s3.head_bucket(Bucket=bucket_name)
        
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = e.response['Error']['Code']
        if error_code == '404':
            exists = False
        s3.create_bucket(Bucket=bucket_name,
                             CreateBucketConfiguration={'LocationConstraint': MY_REGION})
    return s3_resource.Bucket(name=bucket_name)





# connect to S3
s3 = setup_s3()
create_bucket_if_not_exists(BUCKET_NAME)
