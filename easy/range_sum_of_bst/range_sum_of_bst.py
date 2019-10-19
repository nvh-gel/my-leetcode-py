# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23

# Note:
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None or root.val == None:
            return 0

        value = 0
        if root.val >= L and root.val <= R:
            value = root.val

        if root.left == None and root.right == None:
            return value
        else:
            return value + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

solution = Solution()

root = TreeNode(10)
root.left= TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(None)
root.right.right = TreeNode(18)
output = solution.rangeSumBST(root, 7, 15)
print(output)

root = TreeNode(10)
root.left= TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(None)
root.left.right.left = TreeNode(6)
output = solution.rangeSumBST(root, 6, 10)
print(output)