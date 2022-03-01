import math


def getProductsForPage(jsonObj, pageNumber, itemsPerPage):
    list = jsonObj["productList"]
    listSize = len(list)
    
    if len(list) == 0:
        return jsonObj
        
    totalPages = math.ceil( listSize / itemsPerPage )
    indexToStart =  0 if pageNumber == 0 else itemsPerPage * ( pageNumber ) 
    jsonObjToReturn = {}
    listToReturn = []

    for i in range(indexToStart, indexToStart + itemsPerPage):
        listToReturn.append(list[i])
        if i == listSize-1:
            break

    jsonObjToReturn["productList"] = listToReturn
    jsonObjToReturn["pageNumber"] = pageNumber
    jsonObjToReturn["totalPages"] = totalPages
    jsonObjToReturn["totalElements"] = listSize
    
    return jsonObjToReturn