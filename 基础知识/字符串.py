# Python 3.5.2

# 字符串(String)
# python中单引号和双引号使用完全相同。
print( '这是一个句子。' )
print( "这是一个句子。" )

# 使用三引号('''或""")可以指定一个多行字符串。
paragraph = """这是一个段落，
可以由多行组成"""
print( paragraph )

paragraph = '''这是一个段落，
可以由多行组成'''
print( paragraph )

# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
print( '这是' + '一句话。')
print( ('这是' + '一句话。') * 5 )

# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
str = '中华人民共和国万岁'
print( str[5] )
print( str[-2] )           # 输出字符串倒数第二个字符
print( str[0:-1] )           # 输出第一个到倒数第二个的所有字符
print( str[0] )              # 输出字符串第一个字符
print( str[2:5] )            # 输出从第三个开始到第五个的字符
print( str[2:] )             # 输出从第三个开始的后的所有字符

# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。


# 转义符 '\'
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。 如 r"this is a line with \n" 则\n会显示，并不是换行。
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
x = '这是'; y = '一句话。'; print( x+y )

# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=" "
x="a" ; y="b"
# 换行输出
print( x )
print( y )
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()




