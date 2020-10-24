# 11.py

# 使用{}来创建字典
d = {} # 创建了一个空字典

# 创建一个保护有数据的字典
# 语法：
#   {key：value，key：value}

# 字典的值可以是任意对象
# 字典的键可以是任意的不可变对象(int\ str\ bool\ tuple)
# 字典的键是唯一的,  有重复的话,后面的会覆盖前面的

dict1 = {'name':'孙悟空','age':22,'gender':'男'}

print(dict1)

print(dict1['name'],dict1['age'],dict1['gender'])
# print(dict1['dd'])   ##键不存在的话,KeyError: 'dd'