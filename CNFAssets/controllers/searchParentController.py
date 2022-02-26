from templates import responseTemplates
from constants import resourceConstants as rCnt
from constants import eventConstants as eCnt
from utils import searchUtil

import json

CATEGORY = "category"
SUB_CATEGORY = "sub-category"
PAGE_NUMBER = "pageNumber"


def getSearchResult(event):    

    queryParams = event[eCnt.QUERY_PARAMS]

    if CATEGORY in  queryParams and SUB_CATEGORY in queryParams and PAGE_NUMBER in queryParams:
        body = searchUtil.getProductCategoryMetaData(queryParams[CATEGORY], queryParams[SUB_CATEGORY], int(queryParams[PAGE_NUMBER]))
        return responseTemplates.getBasicResponse(200, responseTemplates.getBasicHeader(), body)


    return responseTemplates.getBasicResponse(405, responseTemplates.getBasicHeader(), "Invalid or missing params ! \n Mandatory Params : \ncategory\nsub-category\npageNumber")
