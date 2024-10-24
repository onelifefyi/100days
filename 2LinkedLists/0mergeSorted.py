# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach:
# First, create a dummy node result & store the head of the dummy in start.
# Compare each of the list's value, add the smaller node to the result list.
# Finally at the end, add the remaining list to the result list.
# And return start.next which contains the merged list.
# Time O(n + m) | Space O(1)
def mergeTwoLists(self, list1, list2):
    result = ListNode()
    start = result
    while list1 and list2:
        if list1.val <= list2.val:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
        result = result.next
    result.next = list1 if list1 else list2
    return start.next