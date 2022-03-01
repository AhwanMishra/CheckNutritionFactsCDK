from templates import responseTemplates
from utils import discountCouponsUtil, commonUtil, paginationUtil
from constants import resourceConstants as rCnt
from constants import eventConstants as eCnt
import json

PAGE_NUMBER = "pageNumber"


def getDiscountCoupons(event):

    queryParams = event[eCnt.QUERY_PARAMS]

    if event[eCnt.HTTP_METHOD] == eCnt.GET:
        
        pageNumber = 0
        
        if queryParams != None and PAGE_NUMBER in queryParams:
            pageNumber = int(queryParams[PAGE_NUMBER])

        jsonObj = commonUtil.getBucketData(rCnt.CNF_DISCOUNT_COUPONS_BUCKET_NAME,
         rCnt.DISCOUNT_JSON_FILE_NAME )

        body = json.dumps(paginationUtil.getProductsForPage(jsonObj, pageNumber, rCnt.ADS_PER_PAGE), indent=1)
        
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
