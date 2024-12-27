'''
@File    :   list_free_eips.py
@Time    :   ${DATE}
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
ACCESS_KEY = config.get('aws-dev','aws_access_key_id')
SECRET_KEY = config.get('aws-dev','aws_secret_access_key')
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

#get eips without IPs
def get_eips_without_ips():
    try:
        ec2 = boto3.client('ec2',config=aws_boto_config(), aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        response = ec2.describe_addresses()
        for address in response['Addresses']:
            if 'PrivateIpAddress' not in address and 'InstanceId' not in address and 'AssociationId' not in address:
                print(address['PublicIp'], address['AllocationId'])
        delete_eip(address['AllocationId'])

    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()

#delete eip
def delete_eip(eip_id):
    try:
        ec2 = boto3.client('ec2', config=aws_boto_config(), aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        print(f"Deleting EIP with Allocation id {eip_id}")
        response = ec2.release_address(
            AllocationId=eip_id
        )
        print(response)
    except botocore.exceptions.ClientError as error:
        raise error
        traceback.print_exc()

if __name__ == '__main__':
    get_eips_without_ips()
