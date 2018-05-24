# Given an array of 2n integers, your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
#   Input: [1,4,3,2]
#
# Output: 4
#   Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

# Note:
#   1）n is a positive integer, which is in the range of [1, 10000].
#   2）All the integers in the array will be in the range of [-10000, 10000].

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


# 知识点
# ① list 的方法，list.sort()。注意，返回值为 None
# ② 函数 range( start, stop, step )，返回是个 range 对象。
#    应用形式可以是 list( range( start, stop, step ) )
class Solution1(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in xrange(0, len(nums), 2):
            result += nums[i]
        return result



# 知识点
# ① 函数 sorted( list )，返回的是个list，不改变原list中的元素顺序。
# ② 列表推导式
class Solution2(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum([nums[i] for i in range(0, len(nums), 2)])


if __name__ == '__main__':
    list = [1,4,3,2]
    print(Solution1().arrayPairSum(list))



















