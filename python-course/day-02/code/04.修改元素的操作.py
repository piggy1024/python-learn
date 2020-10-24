# 04.修改元素的操作.py

# 增删改查四种

stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

stus[0] = 'sunwukong'

print(stus)

# del stus[0]
del stus[0] 
print(stus)
print()

stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']
print('修改前：',stus)

# 通过切片来修改列表
# 在给切片进行赋值时,只能使用序列

stus[0:2] = 'hhh' #字符串是个序列
# 先替换0:2  元素还有多就添加
stus[0:2] = ['牛魔王','红孩儿','二郎神','哮天犬']
#使用stus[n,n]给列表插入元素
stus[1:1] = ['这是插入到index为1的元素']
# stus[n:n:1]  =[]  是将左边列表的所有元素插入到index为n之后的位置
# stus[1:1:1]=


print('修改后：',stus) 


# 通过list()函数可以将一个字符串转换成列表
# 通过 ''.join([列表])可以将一个列表转换为字符串

list_a=["345",'567']
str_a="".join(list_a)
print(type(str_a))
print(str_a)

