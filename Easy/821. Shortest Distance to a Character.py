# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.

# Example 1:
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

# Note:
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.

# 题目翻译
# 给定一个字符串S，和一个字符C。求出S中每个字符到最近的字符C的距离。

# 例子：
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

# 备注：
# S的长度范围 [1, 10000]。
# C是单个字符，并且保证在S中存在。
# S与C中的所有字符都是小写字母。


# Intuition
# For each index S[i], let's try to find the distance to the next character C going left,
# and going right. The answer is the minimum of these two values.

# Algorithm
# When going left to right, we'll remember the index prev of the last character C we've seen. Then the answer is i - prev.
# When going right to left, we'll remember the index prev of the last character C we've seen. Then the answer is prev - i.
# We take the minimum of these two answers to create our final answer.
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans



if __name__ == '__main__':

    S = "loveleetcode"
    C = 'e'


    print(Solution().shortestToChar(S,C))















