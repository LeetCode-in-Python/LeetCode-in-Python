# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Sorting #Heap_Priority_Queue
# #Divide_and_Conquer #Quickselect #LeetCode_75_Heap/Priority_Queue
# #Data_Structure_II_Day_20_Heap_Priority_Queue #Top_Interview_150_Heap
# #Big_O_Time_O(n*log(n))_Space_O(log(n)) #2025_07_25_Time_45_ms_(90.46%)_Space_28.73_MB_(45.18%)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
