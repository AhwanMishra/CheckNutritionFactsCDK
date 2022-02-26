import math

PRODUCTS_PER_PAGE = 8

def getProductsForPage(jsonObj, pageNumber):
    list = jsonObj["productList"]
    listSize = len(list)

    totalPages = math.ceil( listSize / PRODUCTS_PER_PAGE )
    indexToStart =  0 if pageNumber == 0 else PRODUCTS_PER_PAGE *  ( pageNumber ) - 1 
    jsonObjToReturn = {}
    listToReturn = []

    for i in range(indexToStart, indexToStart + PRODUCTS_PER_PAGE):
        listToReturn.append(list[i])

    jsonObjToReturn["productList"] = listToReturn
    jsonObjToReturn["totalPages"] = totalPages
    
    return jsonObjToReturn