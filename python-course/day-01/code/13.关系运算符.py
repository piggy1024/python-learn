
result = 10 > 20
result = 2 > True

result = '2' < '11'   # False
result = '2' > '11'   # True

#  当对字符串进行比较时，实际比较的是字符串的unicode编码
# 利用该特性使用unicode对字符串进行排序（中文不行英文可以）
 
print(int('2')>int('11'))


# （==）相等比较的是值  不是对象的id
print(1 == True)

#  （is not）比较的是id
a = 1 is True
print(a)

print("result = ", result)