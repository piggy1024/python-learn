# 03.不定长参数.py

#  定义一个函数,可以求任意个数字的和

def sum(*nums):
    # 定义一个变量保存j结果
    result = 0
    # 遍历元组元素.并累加
    for i in nums:
        result = result + i
    print(result)

sum(1,2,3)

# 定义函数时,可以在形参前面加个*,这个形参会获取所有的实参

def fn(*a):
    print('a = ', a, type(a))

fn(1,2,3,4,5)


# 带星号的参数只有一个,可以个其它参数配合使用

def fn2(a,b,*c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

# 如果* 不是在最后个参数  则其它参数传值时,必须用关键字传参 



#### 星星型形参  会保存成字典

def  fn3(**a):
    print('a = ', a , type(a))

fn3(b = 1, d= 2, c= 3)


# 参数的解包(拆包)

def fn4(a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
 
 # 创建一个元组
t = (10,20,30)

 # 传递实参时, 也可以在序列类型的参数前添加星号,这会自动将序列的元素

fn4(*t)

# 创建一个字典
d = {'a':100, 'b':200, 'c': 300}

fn4(**def)