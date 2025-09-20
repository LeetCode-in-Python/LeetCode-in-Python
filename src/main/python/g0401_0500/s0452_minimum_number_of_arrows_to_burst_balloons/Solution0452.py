# #Medium #Array #Sorting #Greedy #LeetCode_75_Intervals #Top_Interview_150_Intervals
# #2025_09_20_Time_63_ms_(89.91%)_Space_51.32_MB_(78.21%)

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort by ending points
        points.sort(key=lambda x: x[1])
        
        minArrows = 1
        end = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] > end:
                minArrows += 1
                end = points[i][1]
        
        return minArrows
