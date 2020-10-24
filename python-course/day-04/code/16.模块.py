# 16.模块.py

# 模块(module)

# 采用模块化,将程序分别编写出多个文件中

# 用import引入模块

# 每个模块内部都有一个__name__属性,通过这个属性可以获取这模块的名字

import test_module  as test

print(test)
print(__name__)#__main__


