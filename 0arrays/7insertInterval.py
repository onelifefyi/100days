# https://leetcode.com/problems/insert-interval/
# Approach:
# Keep updating the newInterval
# If newInterval ends before the interval starts, insert it first & insert the rest of the intervals to res & break
# If newInterval starts after the interval ends, insert the interval to res & break
# Otherwise (If they merge) | update the newInterval with the merged range & continue
# Return res
# Time O(n) | Space O(n)
def insertInterval(intervals, newInterval):
    resInterval = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            resInterval += newInterval + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            resInterval += intervals[i][1]
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
    return resInterval

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insertInterval(intervals, newInterval))