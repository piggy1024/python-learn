# z字符串需要用引号引起来

s = 'hello'

# 单引号双引号不能混着用   报错SyntaxError: EOL while scanning string literal
# s ="混着来’

# 三重引号表示长字符串  并且保留格式
s='''
锄禾日当午，
汗滴禾下午，
谁知盘中餐，
粒粒皆辛苦。
'''
# 转义字符  \\ 表示反斜杠
s = "子曰：\”学而时习之\“"

# 可以支持unicode
s = '\u16a1'

print(s)