# https://leetcode.com/problems/middle-of-the-linked-list/

# Approach:
# Have slow and fast pointers.
# Keep moving the fast pointers 2 steps till it reaches the end.
# And move the slow pointer one step at a time.
# Finally return the slow pointer.
# Time O(n) | Space O(1)

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow