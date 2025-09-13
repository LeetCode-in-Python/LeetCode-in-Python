# #Medium #Array #Level_2_Day_17_Interval #Top_Interview_150_Intervals
# #2025_09_13_Time_0_ms_(100.00%)_Space_14.32_MB_(16.54%)

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        l = 0
        r = n - 1
        while l < n and newInterval[0] > intervals[l][1]:
            l += 1
        while r >= 0 and newInterval[1] < intervals[r][0]:
            r -= 1
        res = [[0, 0] for _ in range(l + n - r)]
        for i in range(l):
            res[i] = intervals[i][:]
        res[l][0] = min(newInterval[0], newInterval[0] if l == n else intervals[l][0])
        res[l][1] = max(newInterval[1], newInterval[1] if r == -1 else intervals[r][1])
        for i in range(l + 1, l + n - r):
            j = r + 1 + i - l - 1
            res[i] = intervals[j][:]
        return res
