# 12.字典的使用.py

# 方式一 使用dict()函数来创建字典
d = dict(name = '孙悟空',age = 19, gender = '男')
print(d,type(d))

# 方式二 简化一个包含有双值子序列的序列转换为字典
# 双值序列: 序列中只有两个值
# 子序列:序列中的元素是子元素,即为子序列
#如:[[1,2][2,3]]

d = dict([('name','孙悟饭'),('age',18)])

print(d)


# len()获取字典中键值对的个数
print(len(d))

# in not in 用于字典中检查键是否存在


# 获取键值 语法:d[key]
print(d['name'])


#   get方法 get(key[,default])

print(d.get('name'))
#  get方法若查的键不存在会返回None
print(d.get('none'))

# 修改字典
# d[key] = value  存在就覆盖   不存在就添加


# setdefault()  可以用来向字典中添加key-value
# 如果key存在则,不添加
# 如果key不存在,就添加
result = d.setdefault('name','猪八戒')
result = d.setdefault('hello','猪八戒')
print('result= ', result)


# update([other])
# 将其它的字典中的key-value添加到当前字典中
# 若重复会覆盖
d = {'a':1,'b':2,'c':3}
d1 = {'c':4,'d':5,'f':6}
print('修改前:',d)
d.update(d1)
print('修改后:',d)

# del  可以用来删除字典中的key-value
del d['a']




# popitem()
# 一般会将最后一个键值对和三处
# 删除后会把删除的key-value最为返回值返回
# 返回的是一个元组,元组中有两个元素,第一个删除的key 第二个是value

# d.popitem()

result = d.popitem()
print('result= ',result)
print(d)

# d.pop('键')

# 删除字典中的键值对,并返回删除的value

result = d.pop('b')
print(result)

# d.clear() 用来清空字典


# copy()
# 该方法用于对字典进行浅复制
# 复制以后的对象,和原对象独立,修改一个不会影响另一个
# 注意, 浅复制会简单复制对象内部的值,如果只也是一个可变对象,这个可变对象是不可复制的
d = {'a':1,'b':2,'c':3}
d2 = d.copy()
d2['a'] = 100

print(d)
print(d2)
print(id(d))
print(id(d2))


d = {'a':{'name':'孙悟空','age':18},'b':2,'c':3}
d2 = d.copy()
d2['a']['name'] ='猪八戒'

print(d)
print(d2)

print(id(d))
print(id(d2))