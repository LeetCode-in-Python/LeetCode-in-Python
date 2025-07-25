# #Medium #Top_100_Liked_Questions #Array #Hash_Table #Sorting #Heap_Priority_Queue #Counting
# #Divide_and_Conquer #Quickselect #Bucket_Sort #Data_Structure_II_Day_20_Heap_Priority_Queue
# #Big_O_Time_O(n*log(n))_Space_O(k) #2025_07_25_Time_4_ms_(69.79%)_Space_21.51_MB_(27.28%)

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        freq_map = Counter(nums)
        
        # Create a min heap to store the top k elements
        min_heap = []
        
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Extract the elements from the heap
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        
        # Return the result in descending order of frequency
        return result[::-1]
