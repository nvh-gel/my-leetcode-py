class Solution:
    def toLowerCase(self, str: str) -> str:
        tmp_str = list(str)
        for i, char in enumerate(tmp_str):
            ascii_code = ord(char)
            if 64 < ascii_code and 91 > ascii_code:
                tmp_str[i] = chr(ascii_code + 32)
        return ''.join(tmp_str)

input = 'TEST'
solution = Solution()
output = solution.toLowerCase(input)
print(output)

input = 'Hello'
output = solution.toLowerCase(input)
print(output)