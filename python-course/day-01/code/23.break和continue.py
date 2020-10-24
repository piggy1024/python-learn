# 13.break和continue.py

# break
i = 0 
while  i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print('循环结束')

# continue
j = 0 
while j < 5:
    j += 1
    if j == 3:
        break # 1 2   #continue 1 2 4 5 循环结束    
    print(j)
else:
    print('循环结束')

