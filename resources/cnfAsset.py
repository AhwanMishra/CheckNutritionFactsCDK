
def mainHandler(event, context):
    
    #Print and copy event map to see the details and act accordingly.
    
    #  This function simply returns whatever parameter is passed.
    #  First one for /{test-path} & second one is for /test-path?param1=value
    #  For example /{OM} will return OM & /test-path?param1=OM will return "OM" too.
     
    toReturn = {
        "statusCode" : 200,
        "headers" :
            {
                "Content-Type": "application/json"
            },
        "body" : event['pathParameters']["test-path"] if event["resource"] == '/{test-path}'
        else event['queryStringParameters']["param1"]    #single line if in Python
    }
    return toReturn