# 01.异常.py



# print('hello')
# try:
#     print(10 / 2)  
# except:
#     print('hh') 
# else:
#     print('正常')
# print('nihao')

# print('下面是尝试try异常处理的内容:')

# try:
#     print(10 / 0)
# except:
#     print('程序出错了')
# else:
#     print('程序没问题')

# print('a + 10 =')


def fn():
    print('hello, fn')

    print(10 / 0)

def fn2():
    print('这里是fn2')
    fn()

fn2()
# try:
#     fn()
# except:
#     pass