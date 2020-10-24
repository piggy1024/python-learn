# 04.打开文件.py
#open(file, mode='r', buffering=-1, encoding_=None, errors=None, 
#    newline=None, closefd=True, opener=None)

#  file =要打开的文件的名字(路径)
file_name ='..\\demo.txt'
# file_name =r'..\demo.txt'  这是原始字符串

file_obj = open(file_name)


print(file_obj)