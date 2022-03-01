import json
import boto3

from helpers import discountCouponsHelper
from utils import commonUtil


s3 = boto3.client("s3")



def putDataInBucket(bucketName, fileName, content):
    
    existingData = commonUtil.getBucketData(bucketName, fileName)
    
    contentAsObject = json.loads(content)

    
    for i in range (0,len(contentAsObject)):
        validateResponse = discountCouponsHelper.validateDiscountCoupon(contentAsObject[i])
        
        if discountCouponsHelper.validateDiscountCoupon(contentAsObject[i]) != "OK":
            return validateResponse

        existingData["productList"].append(contentAsObject[i])    

    response = s3.put_object(Bucket=bucketName, Key=fileName, Body=json.dumps(existingData))

    return response

def deleteAllOffers(bucketName, fileName):
    response = s3.put_object(Bucket=bucketName, Key=fileName, Body=json.dumps({"productList" : []}))
    return response
