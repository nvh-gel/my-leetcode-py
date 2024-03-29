# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        curr_sum = 0
        max_so_far = -100000
        for i in range(0, len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_so_far:
                max_so_far = curr_sum
            if curr_sum < 0 and i < len(nums) - 1:
                curr_sum = 0
        return max_so_far

solution = Solution()
# number = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# number = [5,4,-1,7,8]
number = [-1]
res = solution.max_sub_array(number)
print(res)
