# 01.类的简介.py

# 定义一个简单的类
# 使用class关键字来定义
# 基本结构:
    # 1.class 类名([父类])
    # 2.公共的属性...
    # 3.对象的初始化方法
    # def __init__(self, 形参...):
    #     pass
    # 4.对象的方法
    # def method1(self, 形参...):
    #     pass

class MyClass():
    pass

mc = MyClass()


#isinstance()用来检查一个对象是否是一个类的实例

result = isinstance(mc,MyClass)
print('result = ', result)