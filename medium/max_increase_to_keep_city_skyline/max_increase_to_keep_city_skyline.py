# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.
# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
# What is the maximum total sum that the height of the buildings can be increased?

# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
# The grid after increasing the height of buildings without affecting skylines is:
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

# Notes:
# 1 < grid.length = grid[0].length <= 50.
# All heights grid[i][j] are in the range [0, 100].
# All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        sky_line_v = grid[0].copy()
        sky_line_h = []

        for row in grid:
            max_h = 0
            for i, val in enumerate(row):
                if val > max_h:
                    max_h = val
                if val > sky_line_v[i]:
                    sky_line_v[i] = val
            sky_line_h.append(max_h)

        raise_level = 0

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                raise_level += min(sky_line_h[i], sky_line_v[j]) - grid[i][j]

        return raise_level

solution = Solution()

input = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
output = solution.maxIncreaseKeepingSkyline(input)
print(output)

input = [[13,47,91,34,20,33,39,22,80,62],[73,97,88,51,38,36,52,75,25,99],[95,43,32,26,82,74,60,69,59,55],[20,41,77,95,79,46,70,50,17,51],[51,0,93,27,46,41,58,49,8,5],[92,58,38,56,73,93,34,47,23,62],[97,66,57,72,26,46,4,90,82,74],[7,44,67,96,0,82,75,22,53,100],[95,48,46,68,41,53,69,42,13,87],[79,48,96,39,21,35,3,12,22,42]]
output = solution.maxIncreaseKeepingSkyline(input)
print(output)