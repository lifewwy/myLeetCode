# Python 3.5.2

# choice(seq)	从序列的元素中随机挑选一个元素，
# 比如random.choice(range(10))，从0到9中随机挑选一个整数。
# 注意：choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
# seq -- 可以是一个列表，元组或字符串。

import random

print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

# ---------------------------------------------------------------------------------------------------------------------
# randrange()
# random.randrange ([start,] stop [,step])
# 注意：randrange()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
# 参数
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数。

import random as rm

# 从 1-100 中选取一个奇数
print ("randrange(1,100, 2) : ", rm.randrange(1, 100, 2))

# 从 0-99 选取一个随机数
print ("randrange(100) : ", rm.randrange(100))

# ---------------------------------------------------------------------------------------------------------------------
# random() 方法返回随机生成的一个实数，它在[0,1)范围内。

import random

# 第一个随机数
print ("random() : ", random.random())


# ---------------------------------------------------------------------------------------------------------------------
# shuffle( list ) 方法将序列的所有元素随机排序。
# shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

import random as rm

list = [20, 16, 10, 5];
rm.shuffle(list)
print ("随机排序列表 : ",  list)

rm.shuffle(list)
print ("随机排序列表 : ",  list)

# ---------------------------------------------------------------------------------------------------------------------
# 随机数组
# 使用 numpy.random 模块来生成随机数组
# 1、np.random.rand 用于生成[0.0, 1.0)之间的随机浮点数，
# 当没有参数时，返回一个随机浮点数，当有一个参数时，返回该参数长度的一维随机浮点数数组
import numpy as np

a = np.random.rand(10)
print(a)
print(type(a))

# 2、np.random.randn 该函数返回一个样本，具有标准正态分布。
import numpy as np
print( np.random.randn(10) )

# 3、np.random.randint(low[, high, size]) 返回随机的整数，位于半开区间 [low, high)。
import numpy as np
print( np.random.randint(10,50,10) )
print( np.random.randint(10,50,size=20) )

# 4、random_integers(low[, high, size]) 返回随机的整数，位于闭区间 [low, high]。
import numpy as np
print( np.random.random_integers(0,1000,5) )

# 5、np.random.shuffle(x) 类似洗牌，打乱顺序；
# 注意：np.random.shuffle() 直接对原始矩阵进行修改（返回值为NoneType）
import numpy as np
arr = np.arange(10)
print(arr)

np.random.shuffle(arr)  # 直接对原始矩阵进行修改（返回值为NoneType）
print(arr)

# 6、np.random.permutation(x)返回一个随机排列
import numpy as np
print( np.random.permutation(20) )









