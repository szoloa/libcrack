from bs4 import BeautifulSoup as soup
import re

class Rinse:
    def __init__(self, text):
        self.text = text

    def __handle(self):
        if self.text == None:
            print("None")
            return None
        dict = {}
        html_soup = soup(self.text, features='lxml')
        if html_soup.find(class_='floor-area floor-area-14') == None:
            return html_soup.get_text()
        for i in html_soup.find(class_='floor-area floor-area-14').find_all(class_='seat using-icon'):
            try:
                status =  re.findall(r'''"status_name":"(.*?)"''', str(i.get_text), 0)[0]
                id = re.findall(r'''"id":(.*?),''', str(i.get_text), 0)[0]
                dict[id] = status
            except:
                print(i, '失败')
        return dict
    def getStatus(self):
        return self.__handle()