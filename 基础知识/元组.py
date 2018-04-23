# Python 3.5.2

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。
# 元组写在小括号()里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 3)     # 输出三次元组
print (tuple + tinytuple) # 连接元组

# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
# 组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup1 = (50) ; print( type(tup1) )
tup1 = (50,) ; print( type(tup1) )

tup3 = "a", "b", "c", "d"
print( tup3 )

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
print( tup1 + tup2 )

print( 3 in (1, 2, 3) )
for x in (1, 2, 3):    # in tuple
    print( x )

for x in [1, 2, 3]:    # in list
    print( x )

# Python 字典存储无顺序 for in 使用要注意
dict = {'name': 'Peter', 45.3: 'Sam', 89: 52}
for x in dict:                                   # in dictionary
    print( x )                                   # 遍历的是键
    print(x,':',dict[x])                         # 打印键值对

# 一般来说，函数的返回值一般为一个。
# 而函数返回多个值的时候，是以元组的方式返回的。
def example(a,b):
    return (a,b)  # 或者 return a,b

print( type(example(3,4)) )































