# 18.Python标准库.py

# sys模块 它提供变量和函数.获取Python解析器的信息


# 引入sys模块
import sys

# 获取参数
# sys.argv
# print(sys.argv)


# 获取当前使用的模块
# sys.modules
# print(sys.modules)

#pretty print
# import pprint
# pprint.pprint(sys.modules)

# sys.path
# 是一个列表, 列表中保存的是当前命令的所有参数
# pprint.pprint(sys.path)


# sys.platform
# 表示当前python运行的平台

# sys.exit()
# 函数用来退出程序



# os模块  对操作系统进行访问

import os

# os.environ
print(os.environ)


# os.system()
# 可以用来执行操作系统的命令(dir)
# os.system('dir')