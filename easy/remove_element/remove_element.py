from typing import List


class Solution:
    def remove_element(self, number: List[int], val: int) -> int:
        count = 0
        next_idx = 0
        idx = 0
        while idx < len(number) or idx + next_idx < len(number):
            if number[idx] != val:
                idx += 1
                next_idx = 0
                count += 1
                continue
            else:
                next_idx += 1
                if idx + next_idx >= len(number):
                    break
                number[idx + next_idx] += number[idx]
                number[idx] = number[idx + next_idx] - number[idx]
                number[idx + next_idx] -= number[idx]
        number = number[:count]
        return len(number)


nums = [1, 2, 3, 4, 5, 5, 4]

ret = Solution().remove_element(nums, 4)

print(nums)
print(ret)
