# 03.异常抛出.py

def add(a , b):
    if a < 0 or b < 0:
        #raise用于向外部抛出异常,后跟一个异常类或者异常类实例
        # raise Exception
        raise Exception('两个参数中不能有负数!')
        # return  None

    r = a + b
    return r
print(add(-100,22))

# 自定义异常类,只需要创建一个类继承Exception
class Lei(Exception):
    pass