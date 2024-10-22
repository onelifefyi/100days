# https://leetcode.com/problems/move-zeroes/

# Approach:
# Two pointers: slow -> stop if value is zero, fast keep going for each item
# Use the fast pointer to keep moving through the array, if fast is non-zero and slow is zero, swap the values, move slow by 1

def moveZeroes(nums):
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[slow] != 0:
            slow += 1
        elif nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
    return nums
            
nums = [0,1,0,3,12]
print(moveZeroes(nums))