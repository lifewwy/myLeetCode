# 翻译：
# 给出一个长度26的数组widths，保存着26个字母打印出来所需要的的屏幕宽度，而每行屏幕宽度都只有100，
# 超过这个宽度的话，字母只能打印到下一行去，给出一段字符串，求出打印后最后一个字母所在的行数，列数。

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        n = 0
        nRow = 1

        for i in range(len(S)):
            d = widths[(ord(S[i]) - ord('a'))]
            n +=  d
            if n > 100:
                n = d
                nRow += 1

        return nRow, n


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"

print( Solution().numberOfLines(widths,S) )
