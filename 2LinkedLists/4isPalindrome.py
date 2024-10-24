# https://leetcode.com/problems/palindrome-linked-list/

# Approach:
# First, find the midpoint using slow and fast pointer approach
# Then reverse the second half of the list (starting at slow)
# Now, start from slow and head, compare each value till slow list ends 
# Know that, slow will always end first (regardless of odd or even number of elements)
# Return False if value mismatch
# Return True otherwise

# Time O(n) | Space O(1)
def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def isPalindrome(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow = reverse(slow)
    while slow:
        if head.val != slow.val:
            return False
        slow = slow.next
        head = head.next

    