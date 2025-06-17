# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Dynamic_Programming
# #LeetCode_75_DP/1D #Algorithm_I_Day_12_Dynamic_Programming #Dynamic_Programming_I_Day_3
# #Level_2_Day_12_Dynamic_Programming #Udemy_Dynamic_Programming #Top_Interview_150_1D_DP
# #Big_O_Time_O(n)_Space_O(n) #2024_06_09_Time_34_ms_(72.11%)_Space_16.5_MB_(81.74%)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        profit = [0] * len(nums)
        profit[0] = nums[0]
        profit[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            profit[i] = max(profit[i - 1], nums[i] + profit[i - 2])
        
        return profit[len(nums) - 1]
