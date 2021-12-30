from typing import Dict
import boto3
from botocore.exceptions import ClientError


def put(table_name: str, items: Dict):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    response = table.put_item( Item=items)
    return response


def get(table_name: str, filter: Dict): 
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    is_success = False

    try:
        response = table.get_item(Key=filter)
        is_success = True 

        if 'Item' in response: 
            return is_success, response['Item']
        else: 
            return is_success, {}

    except ClientError as e:
        print(e.response['Error']['Message'])
        return is_success, str(e)
        


