with open('./data/txt/{}-{}.txt', 'w', encoding='utf-8') as f:
    f.write(str('ls'))
    print('文件已成功写入', f.name)