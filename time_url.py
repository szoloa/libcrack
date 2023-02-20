import time

def getDay():
    return time.strftime(r'%Y-%m-%d')
def getTime():
    return time.strftime('%H:%M')
def getDay_():
    return time.strftime(r'%Y')+'-'+time.strftime('%m').replace('0','')+'-'+time.strftime(r'%d')
def getDay__():
    return time.strftime(r'%m_%d_%H_%M')
def getUrl(herf = '/api.php/spaces_old'): 
    return r'http://zwyy.lib.ctgu.edu.cn{}?area=14&segment=1316671&day={}&startTime={}&endTime=22:00'.format(herf,getDay(),getTime())