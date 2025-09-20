# #Hard #Array #Sorting #Greedy #Heap_Priority_Queue #Top_Interview_150_Heap
# #2025_09_20_Time_64_ms_(97.22%)_Space_17.66_MB_(87.77%)

from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        from heapq import heappop, heappush
        n = len(profits)

        # maintain a sorted array of projects by cost
        min_cost = sorted(zip(capital, profits))
        pointer = 0 # pointer defines affordable segments
        # maintain a max-heap to sort all affordable proj by profits
        # this is need be update at each iteration as "affordable" changes
        max_heap = []

        for _ in range(k):
            # update the max-heap as wallet w changes
            while pointer < n and min_cost[pointer][0] <= w:
                heappush(max_heap, -min_cost[pointer][1]); pointer += 1
            
            if not max_heap:
                break # bankrupted :(

            # profit from the top-profitable in the max-heap
            w += -heappop(max_heap)

        return w
