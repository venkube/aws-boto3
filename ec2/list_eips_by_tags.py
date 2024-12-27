'''
@File    :   list_free_eips.py
@Time    :   27/12/2024
@Author  :   VenuMadhav Palugula
@Version :   1.0
@Contact :   info.venkube@gmail.com
@Desc    :   None
'''

import boto3
import botocore
from botocore.config import Config
import configparser
import traceback

config = configparser.ConfigParser()
config.read("/Users/venkube/.aws/credentials")
ACCESS_KEY = config.get('aws-test','aws_access_key_id')
SECRET_KEY = config.get('aws-test','aws_secret_access_key')
#aws_region = ast.literal_eval((config.get('aws-dev','aws_region')))
aws_region='us-east-1'


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


def get_eip_by_tags(name_tag_value, environment):
    try:
        ec2 = boto3.client('ec2', config=aws_boto_config(), aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        response = ec2.describe_addresses(
            Filters=[
                {
                     'Name': 'tag:Name',
                     'Values': [name_tag_value]
                },
                {
                    'Name': 'tag:environment',
                    'Values': [environment]
                }
            ]
        )
        for eip in response['Addresses']:
            print(eip['PublicIp'])

    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()


if __name__ == '__main__':
    get_eip_by_tags('web-app','dev')
