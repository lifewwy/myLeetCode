# Python 3.5.2

# 函数参数传递，传可变对象还是传不可变对象

# 在 python 中，类型属于对象，变量是没有类型的：
a = [1,2,3]
a = "Runoob"
# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，
# 而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），
# 可以是指向 List 类型对象，也可以是指向 String 类型对象。


# 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
# 而 list,dict 等则是可以修改的对象。

# 不可变类型：变量赋值 a=5 后再赋值 a=8，这里实际是新生成一个 int 值对象 8，再让 a 指向它，而 5 被丢弃，
# 一旦没有变量引用它，它就变成了孤魂野鬼。
# python 是很吝啬的，它绝对不允许在内存中存在孤魂野鬼。
# 凡是这些东西都被看做垃圾，而对垃圾，python 有一个自动的收回机制。
a = 5; print(id(a)) # id() 函数用于获取对象的内存地址。
a = 8; print(id(a)) # id() 函数用于获取对象的内存地址。

# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
la = [1,2,3,4] ;  print(id(la))
la[2] = 5 ;       print(id(la))

# python 传不可变对象，不会改变被传入的函数外的对象
def ChangeInt( a ):
    print('ida: ', id(a))       # a是b的复制，指向同一个对象 2000
    a = 10000                   # 新生成一个 int 值对象 10000，并让 a 指向它
    print('ida: ', id(a))

b = 2000;        print('idb: ', id(b))
ChangeInt(b);    print('idb: ', id(b))
print( b )       # 结果仍是 2000

# python 传可变对象，可以改变被传入的函数外的对象
def changeme( mt ):            # mt 是 mylist 的复制，指向同一个对象
   print('id_mt: ', id(mt) )
   print('修改传入的列表')
   mt.append([1,2,3,4])        # mt 指向对象的内容被改变，mylist 指向同一个对象
   print ("函数内取值: ", mt)
   print( 'id_mt: ', id(mt) )
   return

mylist = [10,20,30]; print('id_mylist: ', id(mylist))
changeme( mylist );  print ("函数外取值: ", mylist)
print('id_mylist: ', id(mylist))

# ---------------------------------------------------------------------------------------------------------------------

# 参数类型：
# 必需参数
# 关键字参数
# 默认参数
# 不定长参数

# 必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

# 关键字参数
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name);
   print ("年龄: ", age);
   return;

# 调用时参数的顺序与声明时可以不一致
printinfo( age=50, name="runoob" );

# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。
# 默认参数必须放在最后面
# 以下实例中如果没有传入 age 参数，则使用默认值：

def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name);
   print ("年龄: ", age);
   return;

#调用printinfo函数
printinfo( age=50, name="runoob" );
print ("------------------------")
printinfo( name="runoob" );

# 不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数。
# 如果在函数调用时没有指定参数，它就是一个空元组。我们可以不向函数传递未命名的变量。
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50, 32, 85, 67 );  # 传入 6 个参数

# ---------------------------------------------------------------------------------------------------------------------

# 匿名函数
# python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。

sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

# ---------------------------------------------------------------------------------------------------------------------
# 变量作用域
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# 就作用域而言，Python与C有着很大的区别，在Python中并不是所有的语句块中都会产生作用域。
# 只有当变量在Module(模块)、Class(类)、def(函数)中定义的时候，才会有作用域的概念。

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这这些语句内定义的变量，外部也可以访问

if True:
   msg = 'I am from Runoob'

print( msg )

# Python的作用域一共有4种，分别是：
# L （Local）     局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global）    全局作用域
# B （Built-in）  内建作用域

# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，
# 便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

# 1. 局部作用域
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print(x)
    inner()

outer()

# 执行结果为 2，因为此时直接在函数 inner 内部找到了变量 x。


# 2.闭包函数外的函数中
x = 0
def outer():
    x = 1
    def inner():
        i = 2
        print(x)
    inner()

outer()
# 执行结果为 1，因为在内部函数 inner 中找不到变量 x，继续去局部外的局部——函数 outer 中找，这时找到了，输出 1。

# 3.全局作用域

x = 0
def outer():
    o = 1
    def inner():
        i = 2
        print(x)
    inner()

outer()
# 执行结果为 0，在局部（inner函数）、局部的局部（outer函数）都没找到变量 x，于是访问全局变量，此时找到了并输出。

# 4. 内建作用域












