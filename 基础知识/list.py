# Python 3.5.2

list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
list3 = ["a", "b", "c", "d"];

# 访问列表中的值
print ("list1[0]: ", list1[0]) # 列表索引从0开始
print ( list2[2:5] )

# 更新列表
# 你可以对列表的数据项进行修改或更新
list = ['Google', 'Runoob', 1997, 2000];
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

# 删除列表元素
list = ['Google', 'Runoob', 1997, 2000]

print (list)
del list[2]
print ("删除第三个元素 : ", list)

# list的操作符
# + 号用于组合列表，* 号用于重复列表
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print( list1 + list2 )
print( list1*5)
print( 3 in list2 )
for x in [1, 2, 3]: print(x)

L=['Google', 'Runoob', 'Taobao', 1, 2, 3]
print( L[-4] ) # 从右侧开始读取倒数第4个元素
print( L[1:] ) # 输出从第二个元素开始后的所有元素

# 嵌套列表
# 使用嵌套列表即在列表里创建其它列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

# 列表的函数 & 方法
list = [-41, 2, 3, 4, 5, 6, 100 ];
print( len(list) )
print( max(list) )
print( min(list) )

list.append('abc');  print( list )

list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(2, 'Baidu')
print ('列表插入元素后为 : ', list1)

print( list1.index('Baidu')) # 从列表中找出某个值第一个匹配项的索引位置

list = [-41, 2, -500, 4, 5, 6, 100 ];
list.sort(); print( list ) # 对原列表进行排序

list = [i for i in range(0,15)]
print( list )
print( list[2:13:3] ) # list[start:end:span]
print( list[::2] )

# ---------------------------------------------------------------------------------------------------------------------
# 列表推导式
# 列表推导式提供了从序列创建列表的简单途径。
vec = [2, 4, 6]
print( [3*x for x in vec] )
print( [[x, x**2] for x in vec] )
# 这里我们对序列里每一个元素逐个调用某方法：
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print( [weapon.strip() for weapon in freshfruit] )
# 我们可以用 if 子句作为过滤器：
vec = [2, 4, 6]
print( [3*x for x in vec if x > 3] )

# 些关于循环和其它技巧
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print( [x*y for x in vec1 for y in vec2] )
print( [vec1[i]*vec2[i] for i in range(len(vec1))] )
# 列表推导式可以使用复杂表达式或嵌套函数
print( [str(round(355/113, i)) for i in range(1, 6)] )

print( [x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3] )
# 他的执行顺序是
# for x in range[1,5]
#     if x > 2
#         for y in range[1,4]
#             if y < 3
#                 x*y

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)























