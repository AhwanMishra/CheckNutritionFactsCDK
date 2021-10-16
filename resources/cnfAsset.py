from controllers import discount_coupons_controller


def mainHandler(event, context):

    # Print and copy event map to see the details and act accordingly.



    toReturn = {
        "statusCode": 200,
        "headers":
            {
                "Content-Type": "application/json"
            },
        # "body" : event['pathParameters']["test-path"] if event["resource"] == '/{test-path}'
        # else event['queryStringParameters']["param1"]    #single line if in Python
        "body": "Hi !"
    }

    if event["resource"] == "/discount-coupons" or event["resource"] == "/discount-coupons/{promo_code}":
        return discount_coupons_controller.getDiscountCoupons(event)

    return toReturn


# /search?sub-category=organic-produce&filters=low_sodium,low_carb........

# /search?q=food

# /search?q=food&filters=low_sodium,low_carb........

# /discount-coupons

#   cdk bootstrap aws://532317821464/us-west-1
#   cdk deploy
