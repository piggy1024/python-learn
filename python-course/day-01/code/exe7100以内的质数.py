# exe7100以内的质数.py


    i = 2 
while i <= 100:

    #创建一个变量，记录i的状态，默认认为i是质数
    flag = True

    # 判断i是否是质数
    # 获取所有可能成为i的因数的数
    j = 2
    while j < i:
        if i % j == 0:
            flag = False
            
        j += 1

    # 验证结果并输出
    if flag :
        print(i)

    i += 1
