# 格式化字符串
a = 'hello'

a = 'abc' + '哈哈ha ha '

# 字符串不能和其它类型进行拼接

# 下面当时任何类型哦都可以拼接   用逗号隔开 
print('a=' , a) # a= abc哈哈ha ha 

# 在创建字符串时，可以在字符串中指定占位符
# %s 在字符串中表示任意字符
b = 'hello %s '%'孙悟空'
c = 'hi %s '%'你好'					# hello 孙悟空 
c = 'hi %s 我是 %s'%('Tom','孙悟空') # hi Tom 我是 孙悟空

c = 'hello %3.5s'%1234.56  #%3.5字符串长度限制在3-5之间
# %f 是浮点数占位符
c = 'hello %.2f'%123.34
# %d 是整数占位符

# 在字符前面添加一个f来创建一个格式化字符串
# 在格式化字符串中可以直接嵌入变量
c = f'hello {a} {b} '


print(a )
print(b)
print(c)

name ='朱秉文'


print('欢迎',name,'光临！')# 逗号会加空格
print('欢迎'+name+'光临！')
print('欢迎%s光临！'%name)
print(f'欢迎{name}光临！')