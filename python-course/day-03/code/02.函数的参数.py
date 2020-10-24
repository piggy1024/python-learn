# 02.函数的参数.py


# 求三个数的乘积
def  chengfa(a, b, c):
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
    print('a * b * c = ', a*b*c)
chengfa(1, 2, 3)


# 欢迎信息
def  welcome(username):
    print(f'欢迎{username}!!')
welcome('著小强')


# 定义一个函数
def fn(a, b ,c):
    print('a =', a)
    print('b = ',b)
    print('c = ',c)
# 关键字传参
fn(b = 10,a = 2, c = 90)


# 函数可以传任意类型参数
def  fn2(a):
    print('a = ' , a)
b = [123,22]
fn2(b)
fn2(fn)



# 参数若进行i相加要同一类型
def  fn3(a,v):
    print(a + v)
# fn3(123, '123')   会报错



#   a 变 c 不变
def fn4(a):
    # a = 20  # 函数中对形参进行修改 不改变其它的变量(####除了形参是一个对象时#####)
    a[0] = 10
    print('a = ', a, id(a))

c = 10
c = [1,2,3]

# fn4(c.copy())
fn4(c[:])

print('c = ', c, id(c))