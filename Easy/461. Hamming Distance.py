# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 2^31.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.


# 解题思路：
# 此题考察的是知识点是运算符，特别是异或运算符^
# 异或运算符作用为“相同出0，不同出1”，这个特性正好可以用来解题
# 那么正常的思路就是将x，y两数进行异或运算，然后统计1的出现次数
# 解法(Python)：
class Solution1(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count("1");
# 这个解法其实很low的，首先用了bin()函数，作用是将异或结果二进制化为字符串，然后利用字符串函数count统计1出现的次数并输出


# 思路
# 首先要想到异或，对x和y取异或后，结果中所有不同位为1；
# 计算1和1间的最大距离，利用 xor & (xor-1) 抵消掉最右侧的1，迭代之，直到xor变为0.
class Solution2(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #xor is used to identify the different bits
        xor = x ^ y; # so different bits would become 1
        n=0;
        #next, calculate biggest distance
        while xor>0:
            n += 1
            print(bin(xor))
            xor = xor & (xor-1)  # xor & (xor-1): set rightest 1 to 0
        return n;


# 符号 & 是按位 与 运算符
# 符号 |	按位 或 运算符：只要对应的二个二进位有一个为1时，结果位就为1。
# 符号 ^	按位 异或 运算符：当两对应的二进位相异时，结果为1
class Solution3(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        z = x ^ y
        while z:
            distance += 1
            print(bin(z))
            z &= z - 1


        return distance



print( Solution2().hammingDistance(123, 452) )






















