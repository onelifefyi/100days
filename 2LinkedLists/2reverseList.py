# https://leetcode.com/problems/reverse-linked-list/

# Approach:
# Set prev as None
# Each iteration save the next item in temp variable
# Set the curren.next to prev
# set prev = curr
# set curr = temp
# Time O(n) | Space O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev