from bs4 import BeautifulSoup as soup
import re

class Rinse:
    def __init__(self,text):
        self.text = text

    def __handle(self):
        if self.text == None:
            print("None")
            return None
        dict = {}
        html_soup = soup(self.text,features='lxml')
        for i in html_soup.find(class_='col-xs-12 col-sm-10 xiaoqu').find_all(class_='seat using-icon'):
            try:
                status =  re.findall(r'''"status_name":"(.*?)"''',str(i.get_text),0)[0]
                id = re.findall(r'''"id":(.*?),''',str(i.get_text),0)[0]
                dict[id] = status
            except:
                print(i,'失败')
        self.dict = dict
    def getStatus(self):
        self.__handle()
        return self.dict
