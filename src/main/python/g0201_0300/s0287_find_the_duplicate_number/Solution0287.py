# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Two_Pointers #Bit_Manipulation
# #Binary_Search_II_Day_5 #Big_O_Time_O(n)_Space_O(n)
# #2025_07_25_Time_16_ms_(96.25%)_Space_30.09_MB_(49.05%)

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 1)
        for num in nums:
            arr[num] += 1
            if arr[num] == 2:
                return num
        return 0
