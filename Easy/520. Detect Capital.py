# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#   1.All letters in this word are capitals, like "USA".
#   2.All letters in this word are not capitals, like "leetcode".
#   3.Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

# Example 1:
# Input: "USA"
# Output: True

# Example 2:
# Input: "FlaG"
# Output: False

# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = 0
        p = []
        for i in range(len(word)):
            if word[i].isupper():
                n += 1
                p.append(i)

        if n==len(word):
            return True
        elif n==0:
            return True
        elif n==1 and p[0]==0:
            return True
        else:
            return False


# 网络答案
class Solution2(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()


print(Solution().detectCapitalUse('FlaG'))
print(Solution().detectCapitalUse('USA'))
print(Solution().detectCapitalUse('Flag'))
print(Solution().detectCapitalUse('leetcode'))


print(Solution2().detectCapitalUse('FlaG'))
print(Solution2().detectCapitalUse('USA'))
print(Solution2().detectCapitalUse('Flag'))
print(Solution2().detectCapitalUse('leetcode'))





















