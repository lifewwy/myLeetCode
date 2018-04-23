# Python 3.5.2

# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *


# import xx 导入模块，对于模块中的函数，每次调用需要“模块.函数”来用。
# from xx import fun 直接导入模块中某函数，直接fun()就可用。
# 告诉你大法：from xx import * 该模块中所有函数可以直接使用。

# import Module               # 引入模块
# from Module import Other    # 引入模块中的类、函数或者变量
# from Module import *        # 引入模块中的所有‘公开’成员
# 其区别就是:
# 第一个：引入的模块(假如是 mdemo )会自动生成一个‘对象‘以模块名命名，然后就可以通过这个‘对
#       象’(mdemo)获取该模块里面的类、函数或变量等...
# 第二个：引入模块中的Other(这里的Other就是模块中定义的成员)成员，调用时就可以省略 模块名。
# 第三个：这种情况如果上面的第二个弄懂的话就不难理解了,其意思就是引入模块中所有'公开'的成员。

import sys
print( sys.argv[0] ) # sys.argv[0]表示代码本身文件路径

from numpy import arange
print( arange(15) )

import numpy as np
a = np.arange(15)
print( a )

from numpy import *
a = array([1, 5, 4, 3])
print( a )

# 一般说来，应该避免使用from...import而使用import语句，
# 因为这样可以使你的程序更加易读，也可以避免名称的冲突
# from ... import 可能会导致命名冲突
# 假设 module a 和 b有2个一样的函数fun()，后使用的 from ... import 会覆盖之前fun()会覆盖之前的。

