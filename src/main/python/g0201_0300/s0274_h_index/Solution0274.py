# #Medium #Array #Sorting #Counting_Sort #Top_Interview_150_Array/String
# #2025_09_17_Time_0_ms_(100.00%)_Space_18.16_MB_(39.50%)

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        freq = [0] * (n + 1)
        for c in citations:
            freq[min(c, n)] += 1
        total = 0
        for h in range(n, 0, -1):
            total += freq[h]
            if total >= h:
                return h
        return 0
