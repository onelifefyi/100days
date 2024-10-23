# https://leetcode.com/problems/insert-interval/
# Approach:
# Keep updating the newInterval
# If newInterval ends before the interval starts, insert it first & insert the rest of the intervals to res & return
# If newInterval starts after the interval ends, insert the interval to res & break
# Otherwise (If they merge) | update the newInterval with the merged range & continue
# Now, if it exits the loop, without inserting the newInterval, that means it's outside the given range, insert the newInterval
# to the result and return
# Time O(n) | Space O(n)
def insertInterval(intervals, newInterval):
    resInterval = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            resInterval += [newInterval] + intervals[i:]
            return resInterval
        if newInterval[0] > intervals[i][1]:
            resInterval += [intervals[i]]
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
    # newInterval is merged when it never get's merged in the loop above
    # That means it's outside the given range
    resInterval += [newInterval]
    return resInterval

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
intervals = []
newInterval = [5,7]
print(insertInterval(intervals, newInterval))