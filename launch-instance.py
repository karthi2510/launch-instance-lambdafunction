import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):
    init_script = """#!/bin/bash
yum update -y
yum install -y httpd
service httpd start
chkconfig httpd on
echo “Hello World from $(hostname -f)” > /var/www/html/index.html"""

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
        UserData=init_script
    )

    print("New instance created:", instance[0].id)