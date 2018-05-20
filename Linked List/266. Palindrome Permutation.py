# Given a string, determine if a permutation of the string could form a palindrome.
#
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
#
# Hint:
#
# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?

class Solution(object):
    def canPermutePalindrome(self, s):
        return sum(s.count(i)%2 for i in set(s))<=1

print(Solution().canPermutePalindrome('code'))
print(Solution().canPermutePalindrome('aab'))
print(Solution().canPermutePalindrome('carerac'))