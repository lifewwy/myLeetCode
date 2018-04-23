# Python 3.5.2

# 实现对复杂字符串的分析并提取出相关信息

# 1、首先要导入python的re模块。
# 2、元字符 . ^ $ * + ? {} [] \ | ()

# re模块里的主要方法：findall()、finditer()、match()、
# search()、compile()、split()、sub()、subn()

import  re

str1 = 'dit dot det,dct dit dot'
print(re.findall('dit',str1))
print(re.findall('dit|dct',str1))

# []作用：[ic]表示i或c，例如'd[ic]t'表示dit和dct两者，和'dit|dct'等价：
print(re.findall('d[ic]t',str1))

# ^作用一：[^ic]中^表示否定，即除了i和c
print( re.findall('d[^ic]t',str1) )

# ^作用二：^dit表示子串在开头位置
print(re.findall('^dit',str1))
print(re.findall('^dct',str1))

# $作用：dot$表示子串要在末尾位置
print(re.findall('dot$',str1))
print(re.findall('dct$',str1))

# .作用：d.t表示d与t之间省略了一个任意字符
print(re.findall('d.t',str1))

# +作用：di+t表示d与t之间省略了一个或多个'i'
str1 = 'd dt dit diit det'
print(re.findall('di+t',str1))




