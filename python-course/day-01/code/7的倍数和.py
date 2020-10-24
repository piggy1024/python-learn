# exe3.py

i = 0
sum = 0
count = 0
while i < 100 :
    i += 1
    if i % 7 == 0 :
        count += 1
        sum += i
print(f'100以内的所有的7的倍数之和：{sum}')
