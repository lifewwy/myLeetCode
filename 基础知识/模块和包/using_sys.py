# import 语句
# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句
# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。
# sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n')
for p in sys.path:
    print(p)

# print('\n\nPython 路径为：', sys.path, '\n')
