import json
def sendResJson(data, code):
    if code == 200:
        return json.dumps(
            {
                'code': code,
                'data':data
            }
        )
    if code == 404:
        return json.dumps(
            {
                'code': code,
                'message': "Not Found"
            }
        )
    else:
        return json.dumps(
            {
                'code': code,
                'message': "Error!"
            }
        )