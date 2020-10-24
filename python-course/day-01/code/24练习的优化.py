# 24练习的优化.py

# 第一次优化是使用break
# 第二次优化是减少找的可能因数的范围即 2~找的数开根号

# 模块 通过模块可以对python进行拓展
# 引入一个time模块， 来统计程序执行的时间
from time import *
# time()函数可以用来获取当前的时间，返回的单位是秒

begin = time()

i = 2 
while i <= 10000:
    flag = True
    j = 2
    while j <= i**0.5:  #当j <  i**2   性能更加优化, 但是必须加=即<=  (为了排除4)
        if i % j == 0:
            flag = False
            # 一旦进入判断，则证明i一定不是质数，此时，内层循环可以退出
            break
        j += 1
    if flag :
        pass
        # print(i)
    i += 1

end = time()

print('程序执行时间为：',end - begin,'秒')