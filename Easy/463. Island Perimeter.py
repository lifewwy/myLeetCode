#
# You are given a map in form of a two-dimensional integer grid where 1 represents land
# and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island
# (i.e., one or more connected land cells). The island doesn't have "lakes"
# (water inside that isn't connected to the water around the island).
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.
#
# Example:
#
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# import webbrowser
# webbrowser.open("https://leetcode.com/static/images/problemset/island.png")
# webbrowser.open("https://leetcode.com/problems/island-perimeter/description/")

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        weight = len(grid[0]) if height else 0
        ans = 0
        for h in range(height):
            for w in range(weight):
                if grid[h][w] == 1:
                    ans += 4
                    if h > 0 and grid[h - 1][w]:
                        ans -= 2
                    if w > 0 and grid[h][w - 1]:
                        ans -= 2
        return ans



x = [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

print(Solution().islandPerimeter(x))









