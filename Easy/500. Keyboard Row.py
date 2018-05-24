
# Given a List of words, return the words that can be typed using letters of alphabet on
# only one row's of American keyboard like the image below.
#
#
# American keyboard
# import webbrowser
# webbrowser.open("https://leetcode.com/static/images/problemset/keyboard.png")


# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [set('qwertyuiop'), set('asdfghjkl'),set('zxcvbnm')]

        # return [ word for word in words
        #         if (set(word.lower())<=keyboard[0]) |
        #          (set(word.lower())<=keyboard[1]) |
        #          (set(word.lower())<=keyboard[2])   ]

        return [ word for word in words
                 for i in keyboard
                 if set(word.lower())<=i ]


words = ["Hello", "Alaska", "Dad", "Peace"]
print(Solution().findWords(words))
























