import json

def parse_request_data(request):
    try:
        request_data = json.loads(request.body)
        request_data.update(request.GET.dict())
        return request_data
    except:
        return None