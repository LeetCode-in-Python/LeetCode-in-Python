# #Easy #Top_100_Liked_Questions #Array #Two_Pointers #LeetCode_75_Two_Pointers
# #Algorithm_I_Day_3_Two_Pointers #Programming_Skills_I_Day_6_Array #Udemy_Arrays
# #Big_O_Time_O(n)_Space_O(1) #2025_07_25_Time_3_ms_(80.05%)_Space_18.63_MB_(94.75%)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(first_zero, i, nums)
                first_zero += 1

    def swap(self, index1: int, index2: int, nums: List[int]) -> None:
        nums[index1], nums[index2] = nums[index2], nums[index1]
