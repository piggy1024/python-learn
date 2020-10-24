# exe4.py
i = 999

# print(i%100)  # 99
# print(int(999/100))  # 9

print('所有的水仙花数如下：')
while i > 100:
    x = int(i / 100)  # x // 100 这是整除
    y = int((i-100*x) / 10) 
    z = i - 100 * x - 10 * y
    if (x**3 + y**3 + z**3) == i :
        print(i)
    i = i - 1