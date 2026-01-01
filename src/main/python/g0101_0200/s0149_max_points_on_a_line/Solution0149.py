# #Hard #Top_Interview_Questions #Array #Hash_Table #Math #Geometry #Algorithm_II_Day_21_Others
# #Top_Interview_150_Math #2025_09_20_Time_59_ms_(34.87%)_Space_17.88_MB_(73.72%)

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = min(len(points), 2)
        n = len(points)
        for i in range(n):
            hashmap = {}
            for j in range(n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x2 - x1 == 0:
                    m = float("inf")
                else:
                    m = (y2 - y1) / (x2 - x1)
                if m in hashmap:
                    hashmap[m].add(i)
                    hashmap[m].add(j)
                else:
                    hashmap[m] = {i, j}
                result = max(len(hashmap[m]), result)
        
        return result
