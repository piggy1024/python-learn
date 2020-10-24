# python中使用变量 不需要声明 直接未变量赋值即可
a = 10
# 如果使用没有赋值过的变量 会报错 NameError: name 'b' is not defined
# 如果多了缩进会   报错  IndentationError: unexpected indent


# 标识符必须遵循标识符的规范
# 标识符中可以含有字母、 数字、 _、,但不能使用数字开头
# 1标识符不能是python中的关键字和保留字
# 2如果使用不符合标准的标识符，将会报错  SyntaxError： invalid syntax
# 3命名规范：
#      下划线命名法 max_length
#      驼峰命名法 maxLength(帕斯卡命名法)
print(a)
shopLacation = '中国'
shopSum = 100 
print('商店在',shopLacation,'共有',shopSum)
