# Python 3.5.2

# d = {key1 : value1, key2 : value2 }
# 字典的每个键值对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

dict['Age'] = 8;               # 更新 Age
dict['School'] = "菜鸟教程"     # 添加信息

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

dict1 = { 'abc': 123, 98.6: 37 }  # 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
print( dict1[98.6] )              # 数字 98.6 是键

# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("dict['Name']: ", dict['Name'])

# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict = {(1,2,3): 'Runoob', 25.6: 78}     # 用元组和数字充当键
print( dict[(1,2,3)] )
print( dict[25.6] )

# 字典内置函数&方法
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print( len(dict) )
print( str(dict) )           # 输出字典，以可打印的字符串表示。
print( list(dict.keys()) )   # 返回一个字典所有的键
print( list(dict.values()) ) # 返回字典中的所有值


# 判断一个字典是否含有某个键
dict = {'Name': 'Runoob', 'Age': 7, 25: 'First'}
print( 'Age' in dict )
print( 25 in dict )
print( 7 in dict )
if 'Name' in dict:
    print('dict 中含有键 Name')

# items() 方法
# Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
dict = {'Name': 'Runoob', 'Age': 7, 25: 'First'}
a = list( dict.items() )
print( type( a[0] ) )

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
for k,v in dict.items():
    print(k,":",v)

# 字典推导可以用来创建任意键和值的表达式词典
print( {x: x**2 for x in (2, 4, 6)} )

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
print( dict(sape=4139, guido=4127, jack=4098) )

# 构造函数 dict() 直接从键值对元组列表中构建字典
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))





