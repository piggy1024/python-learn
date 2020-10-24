# 05.列表的方法.py
stus = ['孙悟空','猪八戒','沙和尚']
print('原列表:',stus)


# append()
stus.append('唐僧')
print('修改后:',stus)

# insert()
stus.insert(0,'插入的第一位:牛魔王')
print('修改后:',stus)

# extend()
# 使用新的序列开扩展当前序列
# 需要一个序列作为参数,它会将该序列的元素添加进去
stus.extend(['extend添加的元素'])
print('修改后:',stus)


# clear()
# 清空序列


# pop() 
# 删除索引为2的元素     但是它会返回删除的值
a = stus.pop()  # 不带参数删除最后一个并返回它的值   参数是索引
print(a)
print('修改后:',stus)


# remove()
# 根据指定的元素,如果相同的元素有多个,只删除第一个
stus.remove('插入的第一位:牛魔王')
print('修改后:',stus)

# reverse()
stus.reverse()
print('修改后:',stus)

# sort()
# 排序 默认升序  sort(reverse)是降序
my_list = list('akdhb')
print('修改前:',my_list)

my_list.sort()

print('修改前:',my_list)


