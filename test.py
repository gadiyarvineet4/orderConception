import json
from parseRequest import parseRequest
from createOrderRequest import CreateOrderRequest

def test():

    test_data = parseRequest()
    json_data=json.dumps(test_data)
    data=CreateOrderRequest.model_validate_json(json_data)
    print(data.itemLines)

test()