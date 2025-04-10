# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Math #Two_Pointers
# #Algorithm_I_Day_2_Two_Pointers #Udemy_Arrays #Top_Interview_150_Array/String
# #Big_O_Time_O(n)_Space_O(1) #2024_06_09_Time_150_ms_(86.92%)_Space_28_MB_(28.67%)

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
