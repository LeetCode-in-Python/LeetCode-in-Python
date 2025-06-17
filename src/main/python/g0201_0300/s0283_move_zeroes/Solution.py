# #Easy #Top_100_Liked_Questions #Array #Two_Pointers #LeetCode_75_Two_Pointers
# #Algorithm_I_Day_3_Two_Pointers #Programming_Skills_I_Day_6_Array #Udemy_Arrays
# #Big_O_Time_O(n)_Space_O(1) #2024_06_08_Time_113_ms_(97.70%)_Space_17.8_MB_(99.81%)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(firstZero, i, nums)
                firstZero += 1

    def swap(self, index1: int, index2: int, nums: List[int]) -> None:
        nums[index1], nums[index2] = nums[index2], nums[index1]
