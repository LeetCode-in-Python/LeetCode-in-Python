# #Medium #Array #Dynamic_Programming #Backtracking #Big_O_Time_O(n*(sum+s))_Space_O(n*(sum+s))
# #2025_07_25_Time_59_ms_(77.59%)_Space_18.11_MB_(61.50%)

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        s = abs(target)
        
        # Invalid s, just return 0
        if s > total_sum or (total_sum + s) % 2 != 0:
            return 0
        
        target = (total_sum + s) // 2
        dp = [[0] * (len(nums) + 1) for _ in range(target + 1)]
        dp[0][0] = 1
        
        # empty knapsack must be processed specially
        for i in range(len(nums)):
            if nums[i] == 0:
                dp[0][i + 1] = dp[0][i] * 2
            else:
                dp[0][i + 1] = dp[0][i]
        
        for i in range(1, target + 1):
            for j in range(len(nums)):
                dp[i][j + 1] += dp[i][j]
                if nums[j] <= i:
                    dp[i][j + 1] += dp[i - nums[j]][j]
        
        return dp[target][len(nums)]
