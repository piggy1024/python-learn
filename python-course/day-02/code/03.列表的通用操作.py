# 03.列表的通用操作.py


# + 和 *
# +可以将两个列表拼接成一个
my_list = [1,2,3]+ [3,4,5]

my_list = [1,2,3]*3


# in 和not in
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']
# in用来检查是否在列表中
# not in 相反   结果返回布尔值
print('孙悟空' not in stus)

# min()获取列表的最小值(max())

arr = [177,333,54,33,55]
print(min(arr))

# index()   count()  这是两个方法
# 方法和函数基本上是一样,方法必须通过对象.方法的形式调用
# 方法实际上是和对象关系紧密的函数
#  index('猪八戒',3,7)  第二个参数表示查找的起始位置,第三个是结束位置
stus.index('猪八戒')
# count统计列表中出现的多少次的元素
print(stus.count('猪八戒'))

str = 'hello'
print('oh' in str) # False
