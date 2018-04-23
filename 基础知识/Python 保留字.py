# Python 3.5.2

# 标识符
# a. 第一个字符必须是字母表中字母或下划线 _ 。
# b. 标识符的其他的部分由字母、数字和下划线组成。
# c. 标识符对大小写敏感。

# python保留字
# 保留字即关键字，我们不能把它们用作任何标识符名称。
# Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：

import keyword
print( keyword.kwlist )
print( keyword.iskeyword('break') )
print( keyword.iskeyword('end') )
