# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

from collections import defaultdict

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            dict[num] = dict.get(num,0) + 1

        for k,v in dict.items():
            if v==1:
                return k

# from internet

# 说明：
# 根据以下几个原则：
# 1）a ^ a = 0
# 2）a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b
# 交换律 结合律
class Solution2(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result ^ i
        return result

# 在 Python3 里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里,用的话要先引入：
from functools import reduce
import  operator
class Solution3:
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)

class Solution4:
    def singleNumber(self, nums):
        return reduce(lambda x, y : x ^ y, nums)



if __name__ == '__main__':
    print(Solution().singleNumber([1, 1, 2, 2, 3]))
    print(Solution2().singleNumber([1, 1, 2, 2, 3]))
    print(Solution3().singleNumber([1, 1, 2, 2, 3]))
    print(Solution4().singleNumber([1, 1, 2, 2, 3]))