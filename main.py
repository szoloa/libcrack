import requests
from bs4 import BeautifulSoup as soup
from proxy import proxy_http_list
from rinse import Rinse

class Main:
    def __init__(self,url) -> None:
        self.url = url
    def __Request(self):
        cookies = {
            'PHPSESSID':'piub6sp24lsllpe5801lnrlr93',
            'PHPSESSID_NS_Sig':'oenCV6mf2Wdl_1y5',
            'redirect_url':r'%2Fhome%2Fweb%2Fseat%2Farea%2F1'
        }
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
                }
        for i in range(4,15):
            print('第',i,'次')
            try:
                r = requests.get(self.url,headers=headers,cookies=cookies,proxies=proxy_http_list[i],timeout=3000)
                if(r.status_code == 200):
                    return r.text
            except:
                continue
            return None
    def run(self):
        return self.__Request()
if __name__ == '__main__':
    text = Main('http://zwyy.lib.ctgu.edu.cn/web/seat3?area=14&segment=1316670&day=2023-2-19&startTime=10:10&endTime=22:00').run()
    print(Rinse(text).getStatus())