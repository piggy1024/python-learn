# 10.可变对象.py

# 一般给变量赋值时，才是

a = [1,2,3]
b = a
# b[0] = 10
b = [10 , 2, 3]
print('a' , a , id(a))
print('b' , b , id(b))


# == ！= is  is not
# ==  != 比较的是对象的值是否相等
# is  is not  比较的是对象的id是否相等（同一对象）