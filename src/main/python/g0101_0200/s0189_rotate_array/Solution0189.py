# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Math #Two_Pointers
# #Algorithm_I_Day_2_Two_Pointers #Udemy_Arrays #Top_Interview_150_Array/String
# #Big_O_Time_O(n)_Space_O(1) #2025_07_25_Time_3_ms_(74.65%)_Space_25.70_MB_(46.80%)
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        t = n - (k % n)
        self.reverse(nums, 0, t - 1)
        self.reverse(nums, t, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
