# 03.对象的初始化.py
class Person:

    # 在类中可以定义一些特殊方法
    # 特殊方法都是以__开头,__结尾

    def __init__(self , name):
        # print('hello')
        # 通过self向新创建的对象添加属性
        self.name = name
    def say_hello(self):
        print('大家好,我是 %s'%self.name)

# p1 = Person()

# #手动添加name属性
# p1.name = '孙悟空'

# p2 = Person()
# p2.name = '猪八戒'

# p3 = Person()
# p3.name = '沙和尚'

# p3.say_hello()

# 对象创建后面的括号的参数都会依次传到init(第一个对象自身不用传)
p1 = Person( '哈哈')
# 创建对象p1 = Person()的运行流程
#   1.创建一个变量
#   2.在内存重创建一个新对象
#   3.__init__(self)方法执行
#   4.将对象的id赋值给变量


# p1.__init__()
p1.say_hello()