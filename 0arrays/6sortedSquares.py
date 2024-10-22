# https://leetcode.com/problems/squares-of-a-sorted-array/

# Approach:
# Two pointers, left and right, check and compare left and right's abs() value
# Insert the greater one in result (from the end)
# Return the result
# Time O(n) | Space O(n)
def sortedSquares(nums):
    results = [0] * len(nums)
    left, right = 0, len(nums) - 1
    index = len(nums) - 1
    while index >= 0:
        if abs(nums[left]) > abs(nums[right]):
            results[index] = nums[left] ** 2
            left += 1
        else:
            results[index] = nums[right] ** 2
            right -= 1
        index -= 1
    return results


# nums = [-4,-1,0,3,10]
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))
