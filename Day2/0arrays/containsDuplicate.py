# https://leetcode.com/problems/contains-duplicate/

# Approach:
# Use a hashset to keep storing each elements of the array
# If the value already exists return True
# Otherwise return False
# Time O(n) | Space O(n)
def containsDuplicate(nums):
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)
    return False

nums = [1,1,1,3,3,4,3,2,4,2]