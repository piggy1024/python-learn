# 05.文档字符串.py

# help是内置函数

# help(函数对象)





#   文档字符串直接写在函数第一行
def fn(a:int,b:int,c:bool) - > int:
    '''
    这是一个文档字符串示例

    函数的作用是
    函数的参数:
        a,作用, 类型, 默认值....
    '''
    return 10

help(fn)