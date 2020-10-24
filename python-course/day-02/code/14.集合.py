# 14.集合.py
# 使用{}来创建集合


d = [[1,2],[2,3]]
print(d , type(d))


s = {1,5,3,40,1,1,1,1}
print(s, type(s))

# s = {[1,2,3],[1,4,5]} TypeError: unhashable type: 'list'

# 使用set()函数来创建集合
s = {}    #这是空字典
s = set() # 这是空集合


# 可以通过set() 将序列\字符串\字典转化成集合
s = set([1,2,3,4,5])
s = set('hello')
s = set({'a':1,'b':2,'c':3})  # 只会保存键
print(s)


s = {'a','b',1,2,3}
# 将集合转换成列表
print(list(s)[0] , type(s))

# add() 向集合增加元素,无返回值
s.add(10)
print(s)

#update()  将一个集合中元素加到当前集合中
s1 = set('hello')
s.update(s1)
s.update((1,3,2,3))
print(s)

# pop() 随机删除一个集合中的元素,并返回删除的元素
yuans=s.pop()

print(s)
print(yuans)

# remove 删除集合指定的元素

s.remove('o')
print(s)

# clear 清空集合

# copy() 对集合进行浅复制