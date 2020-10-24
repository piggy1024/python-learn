# exe1.py
# ex1
print('请输入一个数字：')
num = int(input('>'))
if num%2 == 0 :
    print(num,  '用户输入的数字为偶数！')
else :
    print(num, '用户输入的数字为奇数！')

# ex2
print('输入一个年份')

year = int(input('>'))

if  year % 4 == 0 and year % 100 != 0 :
    print(year,'年是闰年')
elif year % 400 == 0 :
    print('%s年是闰年'%year)
else :
    print(f"{year}不是闰年")

# exe3

print('请输入狗的年龄：')
dog_age = float(input('>'))
if dog_age <= 0 :
    print('请输入狗的正确年龄！')
elif dog_age <= 2 :
    dog_age *= 10.5
    print(f"狗的年龄是{dog_age}")
else :
    dog_age= 10.5 * 2 + (dog_age - 2)*4
    print(f"狗的年龄是{dog_age}")


# exe4
print('请输入小明的期末成绩：')
score = float(input('>'))

if score == 100 :
    print('奖励BWM')
elif  80<= score <=99 :
    print('奖励iphone一台')
elif 60 <= score <=79 :
    print('奖励参考书一本')
else :
    print('啥都没奖')

# exe5
print('请选择几号男嘉宾：')
number = int(input(">"))

if number == 1 :
    height = 180
    money = 1000
    hansome = 500
elif number == 2 :
    height = 150
    money = 900
    hansome = 400
else :
    height = 150
    money = 1100
    hansome = 400

print("你要嫁给他吗？")
if height >= 180 and money >= 1000 and hansome >=500 :
    print('我一定嫁给他！')
elif not (height >= 180) and not (money >= 1000) and not (hansome >=500) :
    print("不嫁！")
else :
    print("还是嫁了吧！")
