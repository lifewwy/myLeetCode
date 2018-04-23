# Python 3.5.2

import time

# 获取当前时间
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
print( list( localtime ) )

# 获取格式化的时间
# 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

# 格式化日期
# 我们可以使用 time 模块的 strftime 方法来格式化日期，
import time

# 格式化成 2016-03-20 11:45:39 形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成 Sat Mar 28 22:24:24 2016 形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# http://www.runoob.com/python3/python3-date-time.html
import webbrowser
# webbrowser.open("http://www.baidu.com")
webbrowser.open("http://www.runoob.com/python3/python3-date-time.html")
