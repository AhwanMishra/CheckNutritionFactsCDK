from helpers import basic_response_templates
from utils import discount_coupons_util
import json

headers = {
    "Content-Type": "application/json"
}


def getDiscountCoupons(event):

    if event["httpMethod"] == "GET":
        body = json.dumps(discount_coupons_util.getBucketData('cnf-discount-coupons-bucket', "discount.json" ))
        return basic_response_templates.basicResponse(200, headers, body)

    if event["httpMethod"] == "POST":
        body = json.dumps(discount_coupons_util.putDataInBucket('cnf-discount-coupons-bucket', "discount.json", event["body"] ))
        return basic_response_templates.basicResponse(200, headers, body)

    if event["httpMethod"] == "DELETE":
        return basic_response_templates.basicResponse(200, headers, "delete the offer with promo "
        + event['pathParameters']["promo_code"])
    
    


    return basic_response_templates.basicResponse(405, headers, event["httpMethod"] + " is not allowed !")
