# Python 3.5.2

# 多个变量赋值
# Python允许你同时为多个变量赋值
a = b = c = 1

a, b, c = 1, 2, "runoob"

# --------------------------------------------------
# 标准数据类型
# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）
# --------------------------------------------------

# Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
# 内置的 type() 函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 此外还可以用 isinstance 来判断
a = 111
print( isinstance(a, int) )

