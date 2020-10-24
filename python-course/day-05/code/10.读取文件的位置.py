# 10.读取文件的位置.py

# seek(参数1,参数2)  参数1是要切换到哪里  
    # 参数2:
    #     0 从头计算 ,默认值
    #     1 从当前位置计算
    #     2 从最后位置开始计算

# 一个中文三个字节

with open(r'../demo.txt','rb') as file_obj:
    print(file_obj.seek(-10,2))
    print(file_obj.read())
    print('当前读取到哪儿:',file_obj.tell())