# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
#
# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
#
# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
#
# Example 4:
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[3:]
        for i in range(len(b)-1):
            if b[i:i+2] not in ['01','10']:
                return False


        return True

# from internet
class Solution2(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)
        return all (n[x] != n[x + 1] for x in range(len(n) - 1))


# 思路
# 这题是要检查数字的二进制表示中，0和1是不是交错出现的，顺着来一位一位检查就好了。
#
# 考虑从低位向高位检查，每次都要求后一位的值和前一位的值不相同，那么中止条件是什么呢？
# 一个很明显的是后一位和前一位的值相同了，而另一个则是已经到了二进制表示的最高位，即再往后就不再有1了。
#
# 为了代码的简洁，我们可以每次检查数字二进制的最低位的值后，将数字向右移位一位，这样每次都只需要检查
# 二进制最低位就好了。当这个检查过程中止后，就只需要检查当前的数字是不是0（二进制表示不再有1）就好了。


class Solution3(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1  # 取 n 的二进制数的最后一位
        n >>= 1
        while n:
            bit = n & 1
            if bit == last: return False
            last = bit
            n >>= 1
        return True

print(Solution().hasAlternatingBits(5))
print(Solution().hasAlternatingBits(7))
print(Solution().hasAlternatingBits(11))
print(Solution().hasAlternatingBits(10))
print()
print(Solution2().hasAlternatingBits(5))
print(Solution2().hasAlternatingBits(7))
print(Solution2().hasAlternatingBits(11))
print(Solution2().hasAlternatingBits(10))
print()
print(Solution3().hasAlternatingBits(5))
print(Solution3().hasAlternatingBits(7))
print(Solution3().hasAlternatingBits(11))
print(Solution3().hasAlternatingBits(10))