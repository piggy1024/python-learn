# 02.定义类.py

# 定义类的语法  class 类名:
# 类的方法  def 方法名(self)  方法会默认传递一个实参.这个参数是创建的对象

class MyClass:
    name = '孙悟空'

    def say_hi(self):
        print('我是 %s'%self.name)

mc = MyClass()
# mc.name = '孙悟空的滴滴'
mc.say_hi()