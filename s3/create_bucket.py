#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   create_bucket.py
@Time    :   2024/07/13 14:51:09
@Author  :   VenuMadhav Palugula 
@Version :   1.0
@Contact :   info.venkube@gmail.com
@Desc    :   None
'''

import boto3
from botocore.config import Config
import configparser
import ast


config = configparser.ConfigParser()
config.read('aws_credentials.properties')
ACCESS_KEY = config.get('study_account','access_key')
SECRET_KEY = config.get('study_account','secret_key')
aws_region = ast.literal_eval((config.get('study_account','aws_region')))


my_aws_boto_config = Config(
    region_name = aws_region, #specify the AWS region name
    retries = { # Client retry behavior configuration
        'max_attempts': 10,
        'mode': 'standard'
    },
    max_pool_connections = 10 #maximum number of connections to keep in a connection pool.
)

# Creating a session with explicit credentials
session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name= aws_region,
    config = my_aws_boto_config
)

#Intialize the S3 Client
s3_client = session.client('s3')

#Create the S3 Bucket
s3_client.create_bucket(Bucket='Devops-S3-Bucket',ACL='public-read')