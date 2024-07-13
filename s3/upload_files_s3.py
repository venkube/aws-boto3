'''
@File    :   upload_files_s3.py
@Time    :   2024/07/13 17:36:56
@Author  :   VenuMadhav Palugula 
@Version :   1.0
@Contact :   info.venkube@gmail.com
@Desc    :   None
'''

import boto3
import botocore
from botocore.config import Config
import configparser
import ast
import traceback

config = configparser.ConfigParser()
config.read("D:/Study/GitHub/aws-boto3/s3/aws_credentials.properties")
ACCESS_KEY = config.get('study_account','access_key')
SECRET_KEY = config.get('study_account','secret_key')
aws_region = ast.literal_eval((config.get('study_account','aws_region')))

def aws_boto_config():
    try:
        my_aws_boto_config = Config(
            region_name = aws_region, #specify the AWS region name
            retries = { # Client retry behavior configuration
                'max_attempts': 10,
                'mode': 'standard'
            },
            max_pool_connections = 10 #maximum number of connections to keep in a connection pool.
        )
        return my_aws_boto_config
    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()


#Create S3 bucket using resource object
def upload_files_s3_bucket():
    try:
        my_aws_boto_config = aws_boto_config()
        # Creating a session with explicit credentials
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            region_name= aws_region,
        )
        #Intialize the S3 Client
        s3_client = session.client('s3', config=my_aws_boto_config)

        #Upload a file to S3 bucket
        s3_response = s3_client.upload_file(Bucket='my-aws-boto-bucket',Filename='D:/Study/GitHub/aws-boto3/s3/sample-upload.txt', Key='sample-upload.txt')

        print(s3_response)
    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()

#Create S3 bucket using resource object
def download_files_s3_bucket():
    try:
        my_aws_boto_config = aws_boto_config()
        # Creating a session with explicit credentials
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            region_name= aws_region,
        )
        #Intialize the S3 Client
        s3_client = session.client('s3', config=my_aws_boto_config)

        #download a file to S3 bucket
        s3_response = s3_client.download_file(
            Bucket='my-aws-boto-bucket',
            #FilePath to download
            Filename='D:/Study/GitHub/aws-boto3/s3/sample-download.txt',
            #S3 bucket complete path
            Key='sample-upload.txt'
        )

        print(s3_response)
    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()


if __name__ == '__main__':
    upload_files_s3_bucket()
    download_files_s3_bucket()
