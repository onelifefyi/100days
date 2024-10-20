# https://leetcode.com/problems/majority-element/

# Approach:
# Count the number of each num using a frequency table (hashmap)
# now iterate through the freq table, keeping track of max freq & the corrosponding value
# return the corrosponding max value
# Time O(n) | Space O(n)


# Approach:
# This can be done in one pass, where you keep track of the majoriy you have inserted:
# Time O(n) | Space O(n)
def majorityElement(nums):
    freq_table = {}
    max_freq_element = nums[0]
    max_freq = 0
    for num in nums:
        freq_table[num] = freq_table.get(num, 0) + 1
        if freq_table[num] > max_freq:
            max_freq_element = num
            max_freq = freq_table[num]
    return max_freq_element
    

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums=nums))