# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ind1 = [i for i in range(len(words)) if words[i]==word1]
        ind2 = [i for i in range(len(words)) if words[i]==word2]

        print(ind1,ind2)

        return min([abs(i - j) for i in ind1 for j in ind2])

words = ["practice", "makes", "perfect", "coding", "makes"]

word1 = 'coding'; word2 = 'practice'
# word1 = 'makes'; word2 = 'coding'
print(Solution().shortestDistance(words,word1,word2))