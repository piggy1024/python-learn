# 16.运算符的优先级.py

a = 1 + 2 * 3

a = 1 or 2 and 3

print(a)


# 运算符and 要比 or 高级
# 运算符的优先级可以用优先级的表格来查询
# b在表格位置越靠下越高级
print(1 or 2)
print(1 and 2)

# 逻辑运算符可以连着使用
result = 1 < 2 < 3   # 相当于1 < 2  and 2 < 3 

result = 10 < 20 > 15  # 相当于 10 < 20 and 20 > 15

print(result)