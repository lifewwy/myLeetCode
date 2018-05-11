# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self dividing number,
# including the bounds if possible.
#
# Example 1:
# Input:
#   left = 1, right = 22
# Output:
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# Note:
# The boundaries of each input argument are 1 <= left <= right <= 10000.


# 解题思路：
# 蛮力法（Brute Force）

# 知识点
# ① 先建立空列表，然后在末尾不断添加元素。a = [], a.append(n)
# ② 数字转字符串。 str(256.5869)
# ③ 字符串转整数。 int('137')
# ④ 字符串的遍历。 for c in s:
# ⑤ 算数运算符 %  取模 - 返回除法的余数

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True

        """
        Alternate implementation of self_dividing:
        def self_dividing(n):
            x = n
            while x > 0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True
        """
        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans

        # Equals filter(self_dividing, range(left, right+1))



if __name__ == '__main__':

    print(Solution().selfDividingNumbers(1,100))











