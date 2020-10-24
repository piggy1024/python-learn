# 11.文件的其它操作.py

import os
from pprint import pprint

# os.listdir() 沮渠指定目录结构   路径作为参数
# 返回的是一个列表
r = os.listdir()

print(r)


# os.getcwd()  获取当前所在的目录

# os.chdir()   切换目录   

# os.mkdir()  在当前目录创建文件夹
    
# os.rmdir('dd')   删除文件夹dd

# os.remove('aaa.txt')  删除文件aaa.txt

# os.rename('旧名字', '新名字')    重命名  也可以重定向文件