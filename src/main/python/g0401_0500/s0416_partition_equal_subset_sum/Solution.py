# #Medium #Top_100_Liked_Questions #Array #Dynamic_Programming #Level_2_Day_13_Dynamic_Programming
# #Big_O_Time_O(n*sums)_Space_O(n*sums) #2024_06_07_Time_550_ms_(64.93%)_Space_16.6_MB_(92.89%)

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
