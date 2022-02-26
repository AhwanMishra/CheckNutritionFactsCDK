from datetime import datetime

def validateDiscountCoupon(inputObject):

    requiredFields = [ "tag_line" ,"link", "discount_percent","promo_code",
    "category", "advertiser", "end_date"]

    if(inputObject is None):
            return "The schema is null."

    for key in requiredFields:
        if key not in inputObject:
            return "The schema is not as expected. Please recheck."

    return "OK"





# def filterByEndDate(jsonObject):

#     for key in jsonObject:
#         givenTime = jsonObject["key"]["end_date"]
#         if(  datetime.now() >= givenTime ):
#             jsonObject.delete(key)

    
#     return jsonObject

# discountCoupons = {
#     "tag_line" : "Select products from JoFAN.",
#     "link" : "https://amzn.to/3iSq27M",
#     "discount_percentage" : 50,
#     "promo_code" : "50U6ZXFI",
#     "category" : "GROCERY_AND_GOURMET_FOOD",
#     "advertiser" : "Amazon",
#     "start_date" : "Oct 11, 11:59 PM ",
#     "end_date" : "Oct 11, 11:59 PM"
#     }


    
# print(json.dumps(discountCoupons.__dict__))