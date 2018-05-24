# Given an integer array with even length, where different numbers in this array represent
# different kinds of candies. Each number means one candy of the corresponding kind.
# You need to distribute these candies equally in number to brother and sister.
# Return the maximum number of kinds of candies the sister could gain.
#
# Example 1:
# Input: candies = [1,1,2,2,3,3]
# Output: 3
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
# The sister has three different kinds of candies.
#
# Example 2:
# Input: candies = [1,1,2,3]
# Output: 2
# Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
# The sister has two different kinds of candies, the brother has only one kind of candies.
#
# Note:
# The length of the given array is in range [2, 10,000], and will be even.
# The number in given array is in range [-100,000, 100,000].

# 分析
# 设糖果总数为N，种类为M
# 妹妹分得的糖果数量为N/2
# 为了使妹妹得到的种类数最多，优先将每个种类的糖果分一个给妹妹。
# 如果N/2 >= M , 妹妹每种糖果都可以拿到一个
# 如果N/2 < M，妹妹最多只能拿到N/2种糖果。

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(int(len(candies) / 2), len(set(candies)))


print(Solution().distributeCandies([1,1,2,2,3,3]))
print(Solution().distributeCandies([1,1,2,3]))