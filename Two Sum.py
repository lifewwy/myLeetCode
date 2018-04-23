# Python 3.5.2

# URL: https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add
# up to a specific target.
# You may assume that each input would have exactly one solution.
# Example: Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i];
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i


if  __name__    ==  "__main__":
    soln =  Solution()
    print( soln.twoSum([2, 7, 11, 15], 18) )
    




