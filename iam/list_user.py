'''
@File    :   create_iam_user.py
@Time    :   2024/07/13 18:03:10
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
        print(aws_region)
        return my_aws_boto_config
    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()

#List IAM user
def list_iam_user():
    try:
        my_aws_boto_config = aws_boto_config()
        # Creating a session with explicit credentials
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            region_name= aws_region,
        )

        iam_resource = session.resource('iam')

        for user in iam_resource.users.all():
            print(user)
        
    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()


if __name__ == '__main__':
    list_iam_user()