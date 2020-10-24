# 13.字典的遍历.py

# keys()   该方法返回所有的key
# values()  该方法返回所有的value
# items()   该方法返回所有的key-value

d = {'name':'孙悟空','age':18,'gender':'男'}

# 通过遍历d.keys() 来获取所有的键
for k in d.keys():
    print(k)

# 通过遍历d.value() 来获取所有的键
for k in d.values():
    print(k)

# 通过遍历d.items() 来获取所有的键
for 用一个变量去接收的,会变成一个元组(key,value)
    用两个的话,会分别接收,key和value
print(d.items())
for k,v in d.items():
    print(k)
    print(v)
    
    
