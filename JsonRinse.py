import json

def rinse(json_rinse):
    if json_rinse == None:
        return None
    dict = {}
    for i in json.loads(json_rinse)['data']['list']:
        dict[i['name']] = i['status_name']
    return dict