# 06.封装.py
class Rectangle():
    """表示矩形的类"""
    def __init__(self, width , height):
        self.hidden_width = width
        self.hidden_height = height

    def get_width(self):
        return self.hidden_width

    def get_height(self):
        return self.hidden_height

    def set_width(self, width):
        self.hidden_width = width

    def set_height(self, height):
        self.hidden_height = height

    def get_area(self):
         return self.hidden_height * self.hidden_width

r = Rectangle(5 , 2)
r.set_height(19)
r.set_width(29)
# print(r.get_area())


# 双下划线开头的属性是隐藏属性 (实际上是被改成了_类名__属性->>_Person__name)
#  一般将一些私有属性以_开头
class Person():
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self , name):
        self._name =name
 
p  = Person('孙悟空')

print(p._name)
