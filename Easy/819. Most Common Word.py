# Given a paragraph and a list of banned words,
# return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of
# punctuation.
# Words in the paragraph are not case sensitive.
# The answer is in lowercase.
#
# Example:
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent
# non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is
# banned.
#
# Note:
# - 1 <= paragraph.length <= 1000.
# - 1 <= banned.length <= 100.
# - 1 <= banned[i].length <= 10.
# - The answer is unique, and written in lowercase
#   (even if its occurrences in paragraph may have uppercase symbols,
#   and even if it is a proper noun.)
# - paragraph only consists of letters, spaces,
#   or the punctuation symbols !?',;.
# - Different words in paragraph are always separated by a space.
# - There are no hyphens or hyphenated words.
# - Words only consist of letters, never apostrophes or
#   other punctuation symbols.


import string
import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # 去除标点符号
        translator = str.maketrans('', '', string.punctuation)
        paragraph = paragraph.translate(translator)
        l = paragraph.lower().split(' ')
        l1 = [w for w in l if w not in banned]

        c = collections.Counter(l1)
        return c.most_common(1)[0][0]


class Solution2(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lookup = set(banned)
        counts = collections.Counter(word.strip("!?',;.")
                                     for word in paragraph.lower().split())

        result = ''
        for word in counts:
            if (not result or counts[word] > counts[result]) and \
               word not in lookup:
                result = word

        return result

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
print(Solution2().mostCommonWord(paragraph, banned))




print()
# 去除标点符号
# Thanks to Martijn Pieters for this improved version

# This uses the 3-argument version of str.maketrans
# with arguments (x, y, z) where 'x' and 'y'
# must be equal-length strings and characters in 'x'
# are replaced by characters in 'y'. 'z'
# is a string (string.punctuation here)
# where each character in the string is mapped
# to None
translator = str.maketrans('', '', string.punctuation)

# This is an alternative that creates a dictionary mapping
# of every character from string.punctuation to None (this will
# also work)
#translator = str.maketrans(dict.fromkeys(string.punctuation))

s = 'string with "punctuation" inside of it! Does this work? I hope so.'

# pass the translator to the string's translate method.
print(s.translate(translator))

# 统计元素出现的频率
from collections import Counter
x = [1,2,3,2]
print(Counter(x))




































