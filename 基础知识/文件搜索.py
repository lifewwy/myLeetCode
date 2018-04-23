# Python 3.5.2

import glob

# 获取指定目录下的所有图片
# print(glob.glob(r"E:/Picture/*/*.jpg"))
print(glob.glob(r"/Users/wyw/PycharmProjects/LeetCode/*.py"))

# 获取上级目录的所有.py文件
print(glob.glob(r'../*.py'))  #相对路径

print(glob.glob('*.py'))

# glob.iglob
# 当前目录中的.py文件
f = glob.iglob('*.py')
for py in f:
    print(py)
