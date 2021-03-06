# 09.元组.py

# 元组是一个不可变的序列
# 它的操作方式基本上和列表是一致的

# 什么时候使用呢?  当我们希望数据不改变时,就使用元组,其余情况均使用列表

# 使用（）来创建元组

my_tuple = ()  # 这是一个空元组

my_tuple = (1,2,3,4,5)


# 当元组不是空元组的时候，可以去掉括号,至少有一个逗号
# 比如
my_tuple = 1,2,3,4,5
a,b,c,d,f = my_tuple
print(a)
print(b)
print(c)
print(d)

# 元组是解包(解构)   即将元组当中每一个值给一个变量




# 除了元组可以解包,序列也可以解包


a = 300 
b = 100 
print('交换前:')
print(a , b)

# 交换a b的值

a , b = b , a
print('交换后:')
print(a , b)


# 在对元组进行解包是,变量的个数 =  元组元素个数

my_tuple = 1,2,3,4
a, b, *c = my_tuple
# 这里的c会转成列表  而a,b整除赋值   也可以将*放在其它位置
print('a=',a)
print('b=',b)
print('c=',c)
