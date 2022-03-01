from utils import commonUtil, paginationUtil
from constants import resourceConstants as rCnt
import json


def getProductCategoryMetaData(category, subCategory, pageNumber):
    jsonObj = commonUtil.getBucketData(rCnt.PRODUCT_CATEGORY_METADATA_BUCKET_NAME, category + "/" +subCategory +".json")
    return json.dumps(paginationUtil.getProductsForPage(jsonObj, pageNumber, rCnt.SEARCH_PRODUCTS_PER_PAGE), indent=1)