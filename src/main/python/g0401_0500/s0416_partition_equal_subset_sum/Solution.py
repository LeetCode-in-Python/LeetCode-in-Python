# #Medium #Top_100_Liked_Questions #Array #Dynamic_Programming #Level_2_Day_13_Dynamic_Programming
# #Big_O_Time_O(n*sums)_Space_O(n*sums) #2025_07_25_Time_564_ms_(63.45%)_Space_18.06_MB_(74.36%)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 == 1:
            return False
        sums //= 2
        dp = [False] * (sums + 1)
        dp[0] = True
        for num in nums:
            for i in range(sums, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[sums]
