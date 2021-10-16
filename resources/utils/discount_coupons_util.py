import json
import boto3

from helpers import discount_coupons_helper


s3 = boto3.client("s3")

def getBucketData(bucketName, fileName):
    
    bucket = bucketName
    key = fileName

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())

    return jsonObject

def putDataInBucket(bucketName, fileName, content):
    
    existingData = getBucketData(bucketName, fileName)
    
    contentAsObject = json.loads(content)

    
    for i in range (0,len(contentAsObject)):
        validateResponse = discount_coupons_helper.validateDiscountCoupon(contentAsObject[i])
        
        if discount_coupons_helper.validateDiscountCoupon(contentAsObject[i]) != "OK":
            return validateResponse

        existingData[contentAsObject[i]['promo_code']] = contentAsObject[i]    

    bucket = bucketName
    key = fileName

    response = s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(existingData))

    return response