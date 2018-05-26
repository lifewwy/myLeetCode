# In the following, every capital letter represents some hexadecimal digit from 0 to f.
#
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".
#
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
#
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is,
# it can be represented as some "#XYZ"
#
# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.
# Note:

# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
# Any answer which has the same (highest) similarity as the best answer will be accepted.
# All inputs and outputs should use lowercase letters, and the output is 7 characters.


# 题目大意：
# 给定RGB格式的颜色代码color，求可以简写为'#XYZ'形式的，与之最接近的颜色代码
# color (r, g, b) 与目标 icolor (ir, ig, ib)的距离为 sum((r - ir) ^ 2 + (g - ig) ^ 2 + (b - ib) ^ 2)
#
# 解题思路：
# 蛮力法（Brute Force）
# 枚举'#XYZ'格式的RGB，记录距离的最小值及其对应的RGB

class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def findpos(ic): # color[1:3]

            x = '0123456789abcdef'

            L = [(int('0x'+i+i,16) - int('0x'+ic,16))**2 for i in x]
            posMin = L.index(min(L))
            return x[posMin]+x[posMin]

        return '#' + findpos(color[1:3]) + findpos(color[3:5]) + findpos(color[5:7])




print(Solution().similarRGB("#09f166"))

















