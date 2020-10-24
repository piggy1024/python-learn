# 15.特殊方法.py

# 特殊方法都是用__method__

#  以下均为特殊方法
# object.__add__(self, other)
# object.__sub__(self, other)
# object.__mul__(self, other)
# object.__matmul__(self, other)
# object.__truediv__(self, other)
# object.__floordiv__(self, other)
# object.__mod__(self, other)
# object.__divmod__(self, other)
# object.__pow__(self, other[, modulo])¶
# object.__lshift__(self, other)
# object.__rshift__(self, other)
# object.__and__(self, other)
# object.__xor__(self, other)
# object.__or__(self, other)

# 定义一个Person类

class Person(object):
    """d人类"""
    def __init__(self, name , age):
        self.name = name 
        self.age = age

    def __str__(self):
        return 'Person [name = %s, age = %d]'%(self.name,self.age)

    def __repr__():
        return 'Hello'

    #__gt__会在对象做大于比较时候调用, 返回值就是结果
    def __gt__(self, other):
        return self.age > other.age

    # __bool__

p1 = Person('孙悟空', 18)
p2 = Person('猪八戒', 28)

print(p1)
print(p2)
print(p1 < p2)