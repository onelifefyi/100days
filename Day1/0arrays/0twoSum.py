# https://leetcode.com/problems/two-sum/

# Approach:
# All possible combination of numbers, check if it makes the target
# Time O(n^2) | Space O(1)

# Improvement:
# Use a dictionary to store the (target - num): index for each number
# Each time encountering a number check if num exists (as key) in the dict, if yes, return index & dict[num]
# Time O(n) | Space O(n)
def twoSum(nums, target):
    needed_map = {}
    for i in range(len(nums)):
        if nums[i] in needed_map:
            return [i, needed_map[nums[i]]]
        else:
            needed_map[target - nums[i]] = i

# nums = [2,7,11,15]
# target = 9
# nums = [3,2,4]
# target = 6
nums = [3,3]
target = 6
print(twoSum(nums, target))