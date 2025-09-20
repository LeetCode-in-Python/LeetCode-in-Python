# #Medium #Array #Heap_Priority_Queue #Top_Interview_150_Heap
# #2025_09_20_Time_78_ms_(92.40%)_Space_34.45_MB_(85.02%)

import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        heap = []
        result = []
        
        # Initialize heap with first k pairs from nums1 and first element of nums2
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        # Extract k smallest pairs
        for _ in range(min(k, len(nums1) * len(nums2))):
            if not heap:
                break
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # Add next pair from nums2 if available
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result
