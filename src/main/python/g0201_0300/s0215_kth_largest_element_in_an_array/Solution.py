# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Sorting #Heap_Priority_Queue
# #Divide_and_Conquer #Quickselect #Data_Structure_II_Day_20_Heap_Priority_Queue
# #Top_Interview_150_Heap #Big_O_Time_O(n*log(n))_Space_O(log(n))
# #2024_06_09_Time_446_ms_(79.92%)_Space_29.9_MB_(52.14%)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
