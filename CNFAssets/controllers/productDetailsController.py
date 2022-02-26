import json
from templates import responseTemplates
from constants import resourceConstants as rCnt
from constants import eventConstants as eCnt
from utils import commonUtil


PRODUCT_ID = "productId"

def getProductDetails(event):
    
    fileName = str(event[eCnt.PATH_PARAMS][PRODUCT_ID])+".json"

    body = json.dumps(commonUtil.getBucketData(rCnt.PRODUCT_DETAILS_BUCKET_NAME, 
    fileName ), indent=1)

    return responseTemplates.getBasicResponse(200, responseTemplates.getBasicHeader(), body)

