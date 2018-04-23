# 通常包总是一个目录，可以使用import导入包，或者from ... import ...来导入包中的部分模块。
# 包目录下为首的一个文件便是 __init__.py。然后是一些模块文件和子目录，
# 假如子目录中也有 __init__.py 那么它就是这个包的子包了。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
# 最简单的情况，放一个空的 __init__.py 文件就可以了。当然这个文件中也可以包含一些初始化代码

# 这里给出了一种可能的包结构
# sound/                          顶层包
#       __init__.py               初始化 sound 包
#       formats/                  文件格式转换子包
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  声音效果子包
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  filters 子包
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# 导入方法一，用户可以每次只导入一个包里面的特定模块，比如
# import sound.effects.echo
# 这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# 如果使用形如import item.subitem.subsubitem这种导入形式，
# 除了最后一项，都必须是包，而最后一项则可以是模块或者是包，
# 但是不可以是类，函数或者变量的名字。

# 导入方法二，还有一种导入子模块的方法是:
# from sound.effects import echo
# 这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
# echo.echofilter(input, output, delay=0.7, atten=4)

# 导入方法三，直接导入一个函数或者变量
# from sound.effects.echo import echofilter
# 可以直接使用 echofilter() 函数:
# echofilter(input, output, delay=0.7, atten=4)

# 注意当使用from package import item 这种形式的时候，
# 对应的item既可以是包里面的子包、模块，或者模块中的函数，类或者变量。

















