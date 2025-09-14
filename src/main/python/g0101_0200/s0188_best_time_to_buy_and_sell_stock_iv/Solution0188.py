# #Hard #Array #Dynamic_Programming #Top_Interview_150_Multidimensional_DP
# #2025_09_14_Time_50_ms_(80.74%)_Space_17.88_MB_(83.54%)

from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (k + 1)
        maxdp = [float('-inf')] * (k + 1)
        
        for i in range(1, n + 1):
            maxdp[0] = max(maxdp[0], dp[0] - prices[i - 1])
            for j in range(k, 0, -1):
                maxdp[j] = max(maxdp[j], dp[j] - prices[i - 1])
                dp[j] = max(maxdp[j - 1] + prices[i - 1], dp[j])
        
        return dp[k]
