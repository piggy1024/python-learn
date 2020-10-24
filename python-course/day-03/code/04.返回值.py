# 04.返回值.py

# 通过return来指定函数的返回值
def sum(*nums):
    # 定义一个变量保存j结果
    result = 0
    # 遍历元组元素.并累加
    for i in nums:
        result += i
    return result

print(sum(12,23,45))