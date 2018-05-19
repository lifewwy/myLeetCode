# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        for i in range(int((len(l)+1)/2)):
            l[i], l[~i] = l[~i], l[i]


        return ''.join(l)

# 网络答案
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

s = 'hello'
print(Solution2().reverseString(s))



















