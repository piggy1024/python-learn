# 01.列表的简介.py

# 创建列表,通过[]来创建列表

my_list = [] # 创建了一个空列表

print(my_list,type(my_list))

# 列表存储的数据,我们成为元素

my_list = [10] 

my_list = [10,20,30,40,500]

my_list = [10,'hello',True,None,[1,2,33],print]

# 打印列表中的某个元素  可用list[index]
# 但是当索引值index不存在时,会报错,IndexError:list out of range

# 获取列表的长度   使用函数len()
print(len(my_list))

animals = ['piggy','rabbit','tiger','mouse','cow']

print('列表friends的长度是',len(animals))

for i in range(5):
    print('列表的第%s位是'%(i+1),animals[i])