from helpers import basic_response_templates
from utils import discount_coupons_util
from constants import resource_constants
import json

headers = {
    "Content-Type": "application/json"
}


def getDiscountCoupons(event):

    if event["httpMethod"] == "GET":
        
        body = json.dumps(discount_coupons_util.getBucketData(resource_constants.CNF_DISCOUNT_COUPONS_BUCKET_NAME,
         resource_constants.DISCOUNT_JSON_FILE_NAME ), indent=1)
        
        return basic_response_templates.basicResponse(200, headers, body)

    if event["httpMethod"] == "POST":
        
        body = json.dumps(discount_coupons_util.putDataInBucket(resource_constants.CNF_DISCOUNT_COUPONS_BUCKET_NAME,
         resource_constants.DISCOUNT_JSON_FILE_NAME, event["body"] ), indent = 2)
        
        return basic_response_templates.basicResponse(200, headers, body)

    if event["httpMethod"] == "DELETE":
        
        body = json.dumps(discount_coupons_util.deleteAllOffers(resource_constants.CNF_DISCOUNT_COUPONS_BUCKET_NAME
        , resource_constants.DISCOUNT_JSON_FILE_NAME), indent = 2)

        return basic_response_templates.basicResponse(200, headers, body)

    return basic_response_templates.basicResponse(405, headers, event["httpMethod"] + " is not allowed !")
