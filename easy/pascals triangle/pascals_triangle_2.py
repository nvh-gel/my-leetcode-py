# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        prev = []
        for i in range(0, rowIndex + 1):
            prev = arr
            if i == 0:
                arr.append(1)
            if i == 1:
                arr.append(1)
            if i > 1:
                arr = []
                arr.append(1)
                for j in range(1, len(prev)):
                    arr.append(prev[j] + prev[j-1])
                arr.append(1)
        return arr


sol = Solution()
i = 3
print(sol.getRow(i))
