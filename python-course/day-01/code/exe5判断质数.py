# exe5.py

i = 2
j = 1
while j < 100: 
    while i < j :
        flag = False
        #判断num能否被i整除
        # 如果num能被i整除，则说明num一定不是质数
        if (j % i) == 0 :
            # 一旦进入循环 就不是质数
            print(j)
        i += 1
    j += 1
