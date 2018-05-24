#
# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
#
# Example 1:
#
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
#
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Notes:
#
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            row.reverse()
            for i in range(len(row)):
                row[i] = row[i]^1
        return A

# 网络答案
# Intuition and Algorithm
#
# We can do this in place. In each row, the ith value from the left is equal to the inverse of the ith value from the right.
#
# We use (C+1) / 2 (with floor division) to iterate over all indexes i in the first half of the row, including the center.
#
# In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i] helps us find the ith value of the row, counting from the right.

class Solution1(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in range(int((len(row) + 1) / 2)):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A


if __name__ == '__main__':
    A = [[1,1,0],[1,0,1],[0,0,0]]

    print(Solution().flipAndInvertImage(A))

    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(Solution1().flipAndInvertImage(A))

