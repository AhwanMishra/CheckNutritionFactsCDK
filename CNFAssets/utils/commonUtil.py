import json
import boto3


s3 = boto3.client("s3")

def getBucketData(bucketName, fileName):
    
    bucket = bucketName
    key = fileName

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())

    return jsonObject