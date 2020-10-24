# 15.条件运算符（三元运算符）.py

print('hello') if False else print('你好！')


a = 10
b = 20
print('a的值比较大！') if a > b else print('b的值比较大!')


max = a if a > b else b
print(max)


a = 10 
b = 20
c = 15
max = a if a > b else b
max = max if max > c else max


max = a if a > b and a > c else b if b > c else c


print(max)


