# 09.闭包.py
# 将函数作为返回值返回  也是一种高阶函数
# 这种高阶函数我们也称为闭包\
# 可以将闭包藏一些私有的数据

# 如何形成闭包:# 1.函数嵌套
              # 2.将内部函数作为函数值返回
              # 3.内部函数必须要使用到外部函数的变量

def fn():

    a = 10

    # 函数内部再定义一个函数
    def inner():
        print('我是fn2')

    # 将内部函数 inner作为返回值返回
    return inner

# r是一个函数,是调用fn()后返回的函数
# 这个函数总数能范文到fn()函数内的变量

r = fn()



#求多个数的平均值
# nums = [50,30,42,44]

# 创建一个函数,用来i计算平均值
def make_avg():

    nums=[]

    def avg(m):
        # 将m添加到列表中
        nums.append(m)
        # 求平均值
        return sum(nums)/len(nums)

    return avg

avg = make_avg()

print(type(avg))
print(avg(10))
