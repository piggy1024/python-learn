# 07.文件读取.py

file_name = r'../demo.txt'

with open(file_name, encoding = 'utf-8') as file_obj:

    print(file_obj.readline(),end = '')
    print(file_obj.readline())

    # readlines()
    #该方法用于一行一行的读取内容  将内容放到一个列表

    r = file_obj.readlines()
    print(r) 