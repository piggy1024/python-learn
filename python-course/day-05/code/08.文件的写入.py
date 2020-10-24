# 08.文件的写入.py
file_name = r'../demo.txt'

# 'r' 只读  
# 'w' 只写 
# 'a' 追加
#  r+  即可读又可写  文件不存在不会报错

# 'x' 创建新文件 , 存在的话不会创建    不存在就创建#
with open(file_name,'a' ,encoding = 'utf-8') as file_obj:
    # writr()会返回写字符的大小
    file_obj.write('\n这是增加的内容')
    file_obj.write('Hello, How are you?增加的\n')
    file_obj.write('Hello, How are you?增加的')