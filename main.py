import requests
from bs4 import BeautifulSoup as soup
from proxy import proxy_http_list
from rinse import Rinse
import time_url
import JsonRinse

class Main:
    def __init__(self,url) -> None:
        self.url = url
    def __Request(self):
        cookies = {
            'PHPSESSID':'jt5h2vgdjdriabknpgjkmmi0h4',
            'PHPSESSID_NS_Sig':'oenCV6mfw3olvQ2-',
            'redirect_url':'%/web/seat2/area/5/day/{}'.format(time_url.getDay())
        }
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49',
                    'Referer': 'http://zwyy.lib.ctgu.edu.cn/web/seat2/area/5/day/2023-2-19'
                }
        for i in range(4,15):
            print('第',i,'次')
            try:
                r = requests.get(self.url,headers=headers,cookies=cookies,timeout=3000)
                # print(r.text)
                if(r.status_code == 200):
                    return r.text
            except:
                continue
            return None
    def run(self):
        return self.__Request()
if __name__ == '__main__':
    text_ = Main(time_url.getTime()).run()
    #print(JsonRinse.rinse(text_))
    #print(Rinse(text_).getStatus())
    with open('./data/txt/{}-{}'.format(time_url.getDay(),time_url.getTime()),'w',encoding='utf-8') as f:
        f.write(str(JsonRinse.rinse(text_)))