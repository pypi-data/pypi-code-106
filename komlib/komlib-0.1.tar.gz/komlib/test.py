from aws.dynamo import put, get 
from aws.sqs import send
from aws.s3 import save 

#items = {"newsId": "test3", "title": "test3"}
#response = put(table_name='news', items=items)

"""
filter = {"newsId": "20211228162117278"}
response = get(table_name='news', filter=filter)
print (response)
"""

"""
message = {"hallo2": "hai"}
response = send(queue_name="newsFeature", message_body=message)
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))
"""

bucket = 'kompas-recommendation'
key = 'test/a.json'
data = {"test": "test"}
save(bucket, key, data)


