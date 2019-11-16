# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note
# All given inputs are in lowercase letters a-z.



class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common_pref = ''
        size = len(strs)
        if (size > 1):
            length = len(strs[0])
            for i in range(0, length):
                count = 1
                sub_str = strs[0][:i+1]
                for j in range(1, size):
                    if len(sub_str) > len(strs[j]) or not strs[j].startswith(sub_str):
                        break
                    else:
                        count += 1
                if count == size:
                    common_pref = sub_str
        elif size == 1:
            common_pref = strs[0]
        return common_pref

solution = Solution()

input = ['flower', 'flow', 'flight']
output = solution.longestCommonPrefix(input)
print(output)

input = ["dog","racecar","car"]
output = solution.longestCommonPrefix(input)
print(output)

input = []
output = solution.longestCommonPrefix(input)
print(output)

input = ['c', 'c']
output = solution.longestCommonPrefix(input)
print(output)

input = ["c","acc","ccc"]
output = solution.longestCommonPrefix(input)
print(output)
