def basicResponse(statusCode, headers, body):
    toReturn = {
        "statusCode" : statusCode,
        "headers" : headers,
        "body" : body
    }

    return toReturn;