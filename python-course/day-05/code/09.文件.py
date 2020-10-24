# 09.文件.py
file_name = r'C:/Users/朱秉林/Desktop/python-course/day-05/girl.jpg'

# t  读取文本文件(默认值)
# b  读取二进制文件(非文本文件)

with open(file_name , 'rb')  as file_obj:
    # print(file_obj.read(100))

    new_file = 'aa.jpg'
    # 打开新建都要写内容文件
    with open(new_file, 'wb') as new_obj:
        # 每次读取文件的大小
        chunk = 100 * 1024

        # 不断读取文件, 直到读取完毕
        while True:
            # 将一次读的内容存到content
            content = file_obj.read(chunk)
            # 判断读取的是否有内容
            if not content:
                break

            new_obj.write(content)
