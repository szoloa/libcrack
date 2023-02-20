import json
import requests
import time_url
import JsonRinse


class Main:
    def __init__(self, url) -> None:
        self.url = url

    def __Request(self):
        cookies = {
            'PHPSESSID': '81qn7akl6oae84rbu10vqvc9n6',
            'PHPSESSID_NS_Sig': 'oenCV6mfkT9htAu8',
            'redirect_url': r'/web/seat2/area/5/day/{}'.format(time_url.getDay_())
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49',
            'Referer': time_url.getUrl('/web/seat3'),
            'X-Requested-With': 'XMLHttpRequest'
        }
        for i in range(4, 17):
            print('第', i - 4, '次尝试')
            try:
                r = requests.get(self.url, headers=headers, cookies=cookies, timeout=3000)
                # print(r.text)
                if r.status_code == 200:
                    return r.text
                else:
                    print(r.status_code)
                    continue
            except:
                print('error in requests')
                continue
        return None

    def run(self):
        return self.__Request()


def getData():
    text_ = Main(time_url.getUrl()).run()
    # print(JsonRinse.rinse(text_))
    # print(Rinse(text_).getStatus())
    with open('./data/txt/{}.txt'.format(time_url.getDay__()), 'w', encoding='utf-16') as f:
        f.write(json.dumps(JsonRinse.rinse(text_)))
        print('文件已成功写入', f.name)