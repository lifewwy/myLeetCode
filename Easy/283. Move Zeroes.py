# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

class Solution2(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: 1 if x == 0 else 0)


class Solution3(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0



nums = [0,1,0,3,12,0,0,0,2,5,6,0,7]
Solution().moveZeroes(nums)
print(nums)

nums = [0,1,0,3,12,0,0,0,2,5,6,0,7]
Solution2().moveZeroes(nums)
print(nums)

nums = [0,1,0,3,12,0,0,0,2,5,6,0,7]
Solution3().moveZeroes(nums)
print(nums)