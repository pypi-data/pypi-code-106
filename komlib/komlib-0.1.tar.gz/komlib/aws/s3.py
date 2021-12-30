import json
import boto3 


s3 = boto3.resource('s3')

def save(bucket, key, data):
    s3object = s3.Object(bucket, key)
    s3object.put(Body=(bytes(json.dumps(data).encode('UTF-8'))))