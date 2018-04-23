# import 语句
# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句
# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。
# sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
import sys

print('import 的搜索路径：')
for p in sys.path:
    print(p)

# 当我们要添加自己的搜索目录时，可以通过列表的append()方法；
# 对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append('xxx')
# 这种方法是运行时修改，脚本运行后就会失效的。

# import sys
# # sys.path.append('/Users/wyw/PycharmProjects/LeetCode/基础知识')
# sys.path.append('..') # 添加上层目录
# import list



