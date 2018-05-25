# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        ret = -10
        for i in nums:
            if i==1:
                c += 1
            else:
                if ret < c:
                    ret = c
                c = 0

        return ret

# from internet
class Solution2(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''.join(str(i) for i in nums)
        l = s.split('0')
        ln = []
        for i in l:
            ln.append(len(i))
        return max(ln)


class Solution3(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return max([len(i) for i in bytearray(nums).split(b'\x00')])


print(Solution3().findMaxConsecutiveOnes([1,1,0,0,1,1,1,0]))
