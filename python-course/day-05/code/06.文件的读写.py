# 06.文件的读写.py

file_name = r'../demo.txt'

try:

    # open()  默认以文本文件打开.
    with open(file_name, encoding = 'utf-8') as file_obj :
        # print(file_obj)从\
        chunk  = 100
        while True:
            # 读取chunk大小的内容
            content = file_obj.read(chunk)

        # 检查是否读取到了内容
            if not content:
                break

            print(content,end='')


except FileNotFoundError as e:
    print(f'{file_name} not exit!')

# help(file_obj)

# file_name = r'demo.txt'

# try:

#     # open()  默认以文本文件打开.
#     with open(file_name, encoding = 'utf-8') as file_obj :
#         # print(file_obj)
#         content = file_obj.read(6)
#         content = file_obj.read(6)
#         content = file_obj.read(6)
#         print(content)
        


# except FileNotFoundError as e:
#     print(f'{file_name} not exit!')