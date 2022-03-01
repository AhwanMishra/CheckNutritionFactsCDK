from controllers import productDetailsController, discountCouponsController, searchParentController
from templates import responseTemplates


def handler(event, context):

    if event["resource"] =="/product-details/{productId}":
        return productDetailsController.getProductDetails(event)

    if event["resource"] == "/search":
        return searchParentController.getSearchResult(event)

    if event["resource"] == "/discount-coupons" or event["resource"] == "/discount-coupons/{promo_code}":
        return discountCouponsController.getDiscountCoupons(event)
        
    return responseTemplates.getBasicResponse(405, responseTemplates.getBasicHeader(), "Wrong inputs")


#   cdk bootstrap aws://532317821464/us-west-1
#   cdk deploy
