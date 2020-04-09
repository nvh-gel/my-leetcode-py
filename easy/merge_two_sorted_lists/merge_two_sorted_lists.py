# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_str(self):
        node_str = ''
        node_str += str(self.val)
        if self.next != None:
            node_str += '->'
            node_str += self.next.to_str()
        return node_str


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

solution = Solution()

input1 = ListNode(1)
input1.next = ListNode(2)
input1.next.next = ListNode(4)
print(input1.to_str())
input2 = ListNode(1)
input2.next = ListNode(3)
input2.next.next = ListNode(4)
print(input2.to_str())
output = solution.mergeTwoLists(input1, input2)
print(output.to_str())
