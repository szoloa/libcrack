import matplotlib.pyplot as plt
import json
import numpy as np

class analysis:
    def __getNum(self,dict):
        x_1 = 0 # 空闲数
        x_2 = 0
        for i in dict.items():
            if i[1] == '空闲':
                x_1 += 1
            else:
                x_2 += 1
        # return (x_1,x_2)
        return x_1

    def pie(self,x_1,x_2):
        plt.pie([x_1,x_2],
        labels=['free {}'.format(x_1),'busy {}'.format(x_2)],
        colors=['g','r'],
        autopct='%.2f%%',)
        plt.title("time")
        plt.show()

    def __getDict(self,path):
        with open(path,encoding='utf-16') as f:
            str = json.loads(f.read())
        return str

    # 生成文件相对地址的序列，data是要获取的时间（天），格式为'%m_%d'
    def __list(self,data):
        list = []
        for i in [f"{hour:02d}_{minute:02d}" for hour in range(24) for minute in range(60)]:
            list.append('.\\data\\txt\\txt\\{}_{}.txt'.format(data,i))
        return list

    def num_list(self,data):
        num_list = []
        for i in range(1440):
            try:
                num_list.append(self.__getNum(self.__getDict(self.__list(data=data)[i])))
            except:
                # num_list.append(0)
                # print('{} is something wroung'.format(i))
                pass
        return num_list    
x = np.arange(1361)
y = np.array(analysis().num_list('02_21'))

plt.plot(x,y)
plt.show()