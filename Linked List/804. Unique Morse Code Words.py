# International Morse Code defines a standard encoding where each letter
# is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps
# to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.",
#  "....","..",".---","-.-",".-..","--","-.",
#  "---",".--.","--.-",".-.","...","-","..-",
#  "...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of
# the Morse code of each letter. For example, "cab" can be written as "-.-.-....-",
# (which is the concatenation "-.-." + "-..." + ".-").
# We'll call such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
#
# Note:
# - The length of words will be at most 100.
# - Each words[i] will have length in range [1, 12].
# - words[i] will only consist of lowercase letters.


# 题意：
# 这道题是Easy难度里，目前通过率最高的题目。题目的目标大致是输入一组单词，
# 要求输出单词转换为莫尔斯密码后的unique密码数量。



# 理解问题关键：
# string.join(seq): 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# len({"a","a","b","b"}) = 2
# ord('a')~ord('z')  :  97 ~ 122

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)：
        d = [".-", "-...", "-.-.", "-..", ".",
             "..-.", "--.", "....", "..", ".---",
             "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-",
             "..-", "...-", ".--", "-..-", "-.--",
             "--.."]

        return len( {''.join(d[ord(i) - ord('a')] for i in w) for w in words} )



if __name__ == '__main__':

    words = ["gin", "zen", "gig", "msg"]
    print( Solution().uniqueMorseRepresentations(words))




























