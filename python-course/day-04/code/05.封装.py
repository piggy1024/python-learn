# 05.封装.py


# 如何提供一个getter和setter方法使外部可以f访问到属性
# getter获取对象中的指定属性(get_属性名)

class Dog(object):
    """表示狗的类"""
    def __init__(self, name , age):
        self.hidden_name = name
        self.hidden_age = age

    def say_hello(self):
        print('大家好, 我是%s'%self.hidden_name)

    def get_name(self):
        '''
            用来获取对象的name属性
        '''
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    def get_age(self):
        return self.hidden_age

    def set_age(self, age):
        if age >0:
            self.hidden_age = age

d  = Dog('旺财')
d.name = '小黑'
d.say_hello()
# 调用setter
d.set_name('猪')


d.set_age(-10)