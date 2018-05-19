# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(' ')
        s1 = ''
        for i in range(len(l)):
            l[i] = l[i][::-1]

        return ' '.join(l)

# 网络答案
class Solution2(object):
    def reverseWords(self, s):
        reversed_words = [word[::-1] for word in s.split(' ')]
        return ' '.join(reversed_words)


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
print(Solution2().reverseWords(s))










