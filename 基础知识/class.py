# Python 3.5.2

class testClass(object):                 # 这里有个冒号
    def  __init__(self, name, gender):   # 这里有个冒号
        self.name = name      # 类属性赋值
        self.gender = gender  # 类属性赋值
        print('初始化')

    def abc(self, age):       # 定义类的方法
        print(self.name)      # 访问类属性
        print(age)
        self.age = age        # 类属性赋值
# ---------------------------------------------------------------------------------------------------------------------

testman = testClass('neo','male')  # 类的实例化，__init__ 被自动调用
testman.abc( 42 )                  # 调用类的方法

print( testman.name )
print( testman.gender )
print( testman.age )

testman.name = 'Peter'
print( testman.name )

# ---------------------------------------------------------------------------------------------------------------------
# self
# self 代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别：它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
# 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)

t = Test()
t.prt()

# ---------------------------------------------------------------------------------------------------------------------
# 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，
# 类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
# 类定义
class people:
    #定义基本属性
    name = 'Peter'
    age = 30
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 75
    #定义构造方法
    def __init__(selfddd,n,a,w):
        selfddd.name = n
        selfddd.age = a
        selfddd.__weight = w
    def speak(selfddd):
        print("%s 说: 我 %d 岁，重 %d 公斤" %(selfddd.name,selfddd.age,selfddd.__weight))

# 实例化类
p = people('runoob',10,30)
p.speak()
print( p.name )   # 访问类的属性

# ---------------------------------------------------------------------------------------------------------------------
# 继承
# Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。

class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))


s = student('ken',10,60,3)
s.speak()

# ---------------------------------------------------------------------------------------------------------------------
# 多继承
# Python同样有限的支持多继承形式。

# ---------------------------------------------------------------------------------------------------------------------
# 方法重写
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：

class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')

class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')

c = Child()               # 子类实例
c.myMethod()              # 子类调用重写的方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法

# ---------------------------------------------------------------------------------------------------------------------
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。
# 在类内部的方法中访问时使用 self.__private_attrs。

# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。
# self.__private_methods。


class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url       # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):          # 私有方法
        print('这是私有方法')

    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()          # 正常输出
x.foo()          # 正常输出
# x.__foo()      # 报错
























