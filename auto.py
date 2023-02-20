import main
import time_url
import time

while True:
    print(time_url.getTime())
    try:
        main.getData()
    except:
        print(time_url.getDay__,time_url.getTime,'is something error')
        with open('./data/txt/{}.txt'.format(time_url.getDay__()), 'w', encoding='utf-16') as f:
            f.write(time_url.getDay__ + time_url.getTime + 'is something error')
            print('文件已成功写入', f.name)
    time.sleep(600000)
