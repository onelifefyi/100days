# https://leetcode.com/problems/linked-list-cycle/description/

# Approach:
# Keep storing each of the node in a set.
# If at a point the set already contains the node, then there is a cycle.
# Time O(n) | Space O(n)

# Approach 2:
# Have fast and slow pointers.
# Move fast pointer by 2 steps and slow pointer by 1 step.
# If at a point, both the pointers meet, there is a cycle.
# And if the fast pointer reaches null, then there is no cycle.
# Time O(n) | Space O(1)

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False