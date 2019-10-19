# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

# Constraints:
# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        length = len(s)
        cur_index = 0
        count = 0

        for index in range(0, length, 2):
            if self.isBalanceStr(s[cur_index:index]):
                cur_index = index
                count += 1

        return count

    def isBalanceStr(self, s: str) -> bool:
        l_count = 0
        r_count = 0
        for char in s:
            if char == 'L':
                l_count += 1
            else:
                r_count += 1
        return l_count == r_count

solution = Solution()

input = 'RLRRLLRLRL'
output = solution.balancedStringSplit(input)
print(output)

input = 'RLLLLRRRLR'
output = solution.balancedStringSplit(input)
print(output)

input = 'LLLLRRRR'
output = solution.balancedStringSplit(input)
print(output)
