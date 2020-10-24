# 14.垃圾回收.py

# 垃圾回收就是将垃圾对象从内存中删除

class A:
    def __init__(self):
        self.name = 'A类'

    def __del__(self):
        print('A()对象被删除了~~',self)

a = A()
b = a
print(a.name)

a = None  # 将a设置为了None,此时没任何变量被引用,它就是垃圾了

input('回车键退出')
