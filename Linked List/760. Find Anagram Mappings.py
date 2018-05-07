# Time:  O(n)
# Space: O(n)

# Given two lists A and B, and B is an anagram of A.
# B is an anagram of A means B is made by randomizing the order of the elements in A.
#
# We want to find an index mapping P, from A to B.
# A mapping P[i] = j means the ith element in A appears in B at index j.
#
# These lists A and B may contain duplicates. If there are multiple answers, output any of them.
#
# For example, given
# A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]
#
# We should return
# [1, 4, 3, 2, 0]
# as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4
# because the 1st element of A appears at B[4], and so on.
#
# Note:
# - A, B have equal lengths in range [1, 100].
# - A[i], B[i] are integers in range [0, 10^5].

# 题意
# 有两个元素相同但各元素位置不同的列表A与B,找出列表A中每个元素，在列表B中的下标，最后返回一个标号的列表，还是很简单的一道题。


# class Solution:
#     def anagramMappings(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: List[int]
#         """
#         result = []
#         for x in A:
#             for y in B:
#                 if x == y:
#                     result.append(B.index(y))
#                     break
#         return result


# 上述代码可简写为：

class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        # list.index( value )
        # 函数用于从列表中找出某个值第一个匹配项的索引位置。

        result=[]
        for x in A:
            result.append(B.index(x))
        return result


if __name__ == '__main__':

    A = [12, 28, 46, 32, 50, 50]
    B = [50, 12, 32, 46, 28, 50]

    print( Solution().anagramMappings(A,B) )





















