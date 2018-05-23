# Given two integers L and R, find the count of numbers in the range [L, R]
# (inclusive) having a prime number of set bits in their binary representation.
#
# (Recall that the number of set bits an integer has is the number of 1s
# present when written in binary. For example, 21 written in binary is 10101 which
# has 3 set bits. Also, 1 is not a prime.)
#
# Example 1:
#
# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
# Example 2:
#
# Input: L = 10, R = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime) 1010中有2个1
# 11 -> 1011 (3 set bits, 3 is prime) 1011中有3个1
# 12 -> 1100 (2 set bits, 2 is prime) prime number 素数、质数
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# Note:
#
# L, R will be integers L <= R in the range [1, 10^6].
# R - L will be at most 10000.

import math
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ret = 0
        for i in range(L,R+1):
            # print(i)
            nsb = bin(i).count('1'); #print(nsb)
            n = math.ceil(math.sqrt(nsb))
            if nsb==1:
                pass
            elif nsb==2:
                ret+=1
            else:
                ret += 1
                for j in range(2,n+1):
                    a,b = divmod(nsb,j)
                    if b==0:
                        ret -= 1
                        break


        return ret
# from internet
# Intuition and Approach
#
# For each number from L to R, let's find out how many set bits it has.
# If that number is 2, 3, 5, 7, 11, 13, 17, or 19, then we add one to our count.
# We only need primes up to 19 because R <= 10^6 < 2^20

class Solution2(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in range(L, R+1))


print(Solution().countPrimeSetBits(10,45643))
print(Solution2().countPrimeSetBits(10,45643))