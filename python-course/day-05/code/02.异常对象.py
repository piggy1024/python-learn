# 02.异常对象.py
#可以在异常类后边跟着一个
print('异常出现前:')

try:
    print(c)
    print(10 / 0)
except NameError as e:
    print('出现nameError',e,type(e))
except ZeroDivisionError:
    print('出现错误')
except Exception: 
    print('捕获未知异常')
else :
    pass
finally:
    pass

