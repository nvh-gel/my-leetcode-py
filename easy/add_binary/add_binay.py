# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    reserve = 0
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        a_reverse = a[::-1]
        b_reverse = b[::-1]
        len_max = max(len_a, len_b)
        result = ''
        for i in range(0, len_max):
            char_a = char_b = '0'
            if i < len_a:
                char_a = a_reverse[i]
            if i < len_b:
                char_b = b_reverse[i]
            result += self.addBinaryChar(char_a, char_b)
        result = result[::-1]
        if self.reserve == 1:
            result = '1' + result
        return result

    def addBinaryChar(self, a: str, b: str) -> str:
        if a == b and a == '1':
            if self.reserve == 1:
                return '1'
            self.reserve = 1
            return '0'
        if a == b:
            added = '0'
            if self.reserve == 1:
                added = '1'
            self.reserve = 0
            return added
        if self.reserve == 1:
            return '0'
        return '1'

sol = Solution()
val = sol.addBinary('1111', '11')
print(val)
