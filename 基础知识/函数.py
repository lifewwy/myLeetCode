# Python 3.5.2

# range
# range(start, stop[, step])
# 参数说明：
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

type (range(5))  # 右击鼠标，然后选择 Execute Line in Console
# help( range )    # 右击鼠标，然后选择 Execute Line in Console

print( list(range(5)) )
print( list(range(2,8)))
print( list(range(2,15,3)))

# ---------------------------------------------------------------------------------------------------------------------
# print 函数
print(1, 2, 3, 'a', 'b', [1,2,3], (6,'你好'))

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10000:
    print(b, end=', ')
    a, b = b, a+b













