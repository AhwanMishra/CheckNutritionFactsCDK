from templates import responseTemplates
from utils import discountCouponsUtil, commonUtil
from constants import resourceConstants as rCnt
from constants import eventConstants as eCnt
import json



def getDiscountCoupons(event):

    if event[eCnt.HTTP_METHOD] == eCnt.GET:
        
        body = json.dumps(commonUtil.getBucketData(rCnt.CNF_DISCOUNT_COUPONS_BUCKET_NAME,
         rCnt.DISCOUNT_JSON_FILE_NAME ), indent=1)
        
        return responseTemplates.getBasicResponse(200, responseTemplates.getBasicHeader(), body)

    if event[eCnt.HTTP_METHOD] == eCnt.POST:
        
        body = json.dumps(discountCouponsUtil.putDataInBucket(rCnt.CNF_DISCOUNT_COUPONS_BUCKET_NAME,
         rCnt.DISCOUNT_JSON_FILE_NAME, event[eCnt.BODY] ), indent = 2)
        
        return responseTemplates.getBasicResponse(200, responseTemplates.getBasicHeader(), body)

    if event[eCnt.HTTP_METHOD] == eCnt.DELETE:
        
        body = json.dumps(discountCouponsUtil.deleteAllOffers(rCnt.CNF_DISCOUNT_COUPONS_BUCKET_NAME
        , rCnt.DISCOUNT_JSON_FILE_NAME), indent = 2)

        return responseTemplates.getBasicResponse(200, responseTemplates.getBasicHeader(), body)

    return responseTemplates.getBasicResponse(405, responseTemplates.getBasicHeader(), event[eCnt.HTTP_METHOD] + " is not allowed !")
