# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for c in s:
            if c in parens.values():
                stack.append(c)
            else:
                if len(stack) > 0  and parens.get(c, '') == stack[len(stack) - 1]:
                    stack.pop(len(stack) - 1)
                else:
                    return False
        return len(stack) == 0

solution = Solution()

input = '()'
output = solution.isValid(input)
print(output)

input = "()[]{}"
output = solution.isValid(input)
print(output)

input = "(]"
output = solution.isValid(input)
print(output)

input = "([)]"
output = solution.isValid(input)
print(output)

input = "{[]}"
output = solution.isValid(input)
print(output)

input = "["
output = solution.isValid(input)
print(output)

input = "]"
output = solution.isValid(input)
print(output)
