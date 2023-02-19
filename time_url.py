import time

def getTime(herf = '/api.php/spaces_old'): 
    return r'http://zwyy.lib.ctgu.edu.cn{}?area=14&segment=1316670&day=2023-2-19&startTime={}&endTime=22:00'.format(herf,time.strftime('%H:%M'))