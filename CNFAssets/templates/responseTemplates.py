def getBasicResponse(statusCode, headers, body):
    toReturn = {
        "statusCode" : statusCode,
        "headers" : headers,
        "body" : body
    }

    return toReturn;

def getBasicHeader():
    headers = {
    "Content-Type": "application/json",
    'Access-Control-Allow-Origin': '*'
    }

    return headers;
