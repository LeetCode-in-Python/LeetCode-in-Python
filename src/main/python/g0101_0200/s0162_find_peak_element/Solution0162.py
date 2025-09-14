# #Medium #Top_Interview_Questions #Array #Binary_Search #LeetCode_75_Binary_Search
# #Algorithm_II_Day_2_Binary_Search #Binary_Search_II_Day_12 #Top_Interview_150_Binary_Search
# #2025_09_14_Time_0_ms_(100.00%)_Space_17.82_MB_(61.39%)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            # This is done because start and end might be big numbers, so it might exceed the
            # integer limit.
            mid = start + ((end - start) // 2)
            if nums[mid + 1] > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return start
