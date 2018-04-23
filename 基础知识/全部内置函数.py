# Python 3.5.2

# Python 解释器内置了一些常量和函数，叫做内置常量（Built-in Constants）
# 和内置函数（Built-in Functions），我们怎么得到全部内置常量和函数的名字呢？


for item in dir(__builtins__):
    print(item)

print('\n总数为：' , len( dir(__builtins__) ))




