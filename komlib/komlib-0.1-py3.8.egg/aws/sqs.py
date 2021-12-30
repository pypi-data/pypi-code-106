from typing import Dict
import boto3
import json


# Get the service resource
sqs = boto3.resource('sqs')


def send(queue_name: str, message_body: Dict): 
    # Get the queue
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    # Create a new message
    response = queue.send_message(MessageBody=json.dumps(message_body))
    return response
