# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Sorting #Two_Pointers
# #Data_Structure_II_Day_2_Array #Udemy_Arrays #Big_O_Time_O(n)_Space_O(1)
# #2024_06_09_Time_31_ms_(90.70%)_Space_16.4_MB_(80.54%)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ones = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[zeroes] = 0
                zeroes += 1
            elif nums[i] == 1:
                ones += 1

        for j in range(zeroes, zeroes + ones):
            nums[j] = 1

        for k in range(zeroes + ones, len(nums)):
            nums[k] = 2