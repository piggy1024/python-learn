# 05.关闭文件.py


# 打开文件的标准格式如下:

file_name = r'../demo.txt'

try:
    with open(file_name) as file_obj:
        print(file_obj)
except FileNotFoundError as e:
    print(f'{file_name} not exit!')
else:
    pass
finally:
    pass






file_name = r'../demo.txt'

file_obj = open(file_name)

content = file_obj.read()

print(content)

# close()关闭文件
file_obj.close()


# with ... as语句

with open(file_name) as file_obj :
    # 在with语句中可以直接使用file_obj
    # with 结束 文件自动结束

    print(file_obj.read())