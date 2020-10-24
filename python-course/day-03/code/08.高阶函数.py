# 08.高阶函数.py
# 接受函数作为参数,或者将函数作为返回值的函数是高阶函数


# 创建一个列表
l = [1,2,3,4,5,6,7,8,9,10]



# 函数:检查一个任意数字是不是偶数
def fn2(i):
    if i % 2 == 0:
        return True

    return False
# 函数:判断检查数字是不是大于5
def fn3(i):
    if i > 5:
        return True

    return False

# 定义一个函数,将指定的列表中的偶数保存到新的列表中返回
def fn(func, lst):
    '''
        fn()函数获取所有偶数保存到新列表

        参数:
            lst:要帅选的列表
    '''

    # 创建新列表
    new_list = []

    # 对新列表筛选
    for n in l:
        if func(n):
            new_list.append(n)

    # 返回新列表
    return new_list

def fn4(i):
    if i% 3 == 0:
        return True

    return False

# print(fn(fn4 , l))

# filter() 可从序列中过滤出符合条件的元素,保存到一个新的序列
# 参数:
#   1.函数,根据函数来过滤序列(可迭代的结构)
#   2.需要过滤的序列(可迭代的结构)
# 返回值:
#    过滤后的新序列(可迭代的结构)


# 匿名函数  lambda 函数表达式 ##############################
#  语法: lambda  参数列表:返回值

def fn5(a , b):
    return a + b

# print((lambda a,b : a + b)(10,20))
# 将一个匿名函数赋值给一个变量
lambda a,b : a + b


r = filter(lambda i : i % 3 == 0 , l)
print(list(r))

# map()
# map()函数可以对可迭代对象中的所有的元素进行指定的操作.然后添加到新的对象中返回
l = [1,2,3,4,5,6,7,8,9,10]


# lambda 形参: 返回值
r = map(lambda i : i+1, l)
print(list(r))


# sort()
# 该方法用来对列表中的元素进行排序
# 在sort()可以接受一个关键字参数,key,key是函数名.
l = ['bb','aaaa','c','dddddd','fff']
l.sort(key = len)
print(l)

#sorted()   用法基本和sort()差不多    
# sorted排序不会影响原来的对象,而是返回一个新的对象

l =[2,5,'1',3,'6']

print('排序前:',l)
s = sorted(l,key = str)
print('排序后:',l)
print(s)