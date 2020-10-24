# 07.递归.py


# 尝试求 10!

sum = 1
for i in range(1,11):
    sum *= i
print(sum)




# 递归函数的两个要件
    # 1.基线条件
    #     -- 问题可以被分解为的最小问题,当满足基线条件,递归不再执行
    # 2.递归条件
    #     -- 将问题继续分解的条件

# 10! = 10 * 9!
# 9! = 9 * 8!
# ......
# 2! = 2 * 1!
# 1! = 1
def factorial(n):
    '''
        该函数用来求任意数的阶乘

        参数:
            n为要求阶乘的数字
    '''
    if n == 1:
        # 1的阶乘是1,直接返回1
        return 1
        
    return  factorial(n-1) * n


print(factorial(10))
    

# ex1
def power(n,i):
    '''
        这是一个求n的i次幂的函数
        参数:
            n是底数
            i是幂
    '''
    if i == 1:
        return n

    return power(n,i-1)*n

print(power(3,3))


# ex2
def hui_wen(s):
    '''
        该函数检查指定的字符串是不是回文字符串,是返回True否则False

        参数:
            s:检查的字符串
    '''
    # 先检查第一个和最后一个字符是否一致,一致看倒数第二和第二.
    # 基线条件: 字符串小于2个
    if len(s) < 2:
        # 字符串长度小于2,肯定是回文
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return hui_wen(s[1:-1])

print(hui_wen('abb'))
