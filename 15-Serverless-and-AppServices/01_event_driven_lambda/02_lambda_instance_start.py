import os

import boto3

region = "us-east-1"
ec2 = boto3.client("ec2", region_name=region)


def lambda_handler(event, context):
    instances = os.environ["EC2_INSTANCES"].split(",")
    ec2.start_instances(InstanceIds=instances)
    print("started instances: " + str(instances))
