#14.逻辑运算符.py

a = True
not a  # 对a进行非运算


a = 1
a = not a
print('a = ',a)


result = True and True
result = True and False
result = False and False
result = False and True

print(result)
# 与运算是找False的
# Python中的与运算是短路的与。若第一个值为false，第二个不看
True and print('你猜我能出来不？')
False and print('你猜我能出来不？')


result1 =  True or True # Trur
result1 =  True or False # True
result1 =  False or False # False
result1 = False or True  # True	

print(result1)

# 或运算是找True
True or print('你猜我能出来不？')
False or print('你猜我能出来不？')

#非布尔值的与或运算
# 对非布尔值进行与或运算时，python会将其当作布尔值运算，最终会返回原值

#下面是True and True
print('这是:',1 and 2) # 2
#下面是False and True
print('这是:',0 and 2) # 2
#下面是True and False
print('这是：',1 and 0) #1


print(1 and 0 or 0)