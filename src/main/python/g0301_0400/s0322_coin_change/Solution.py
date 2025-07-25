# #Medium #Top_100_Liked_Questions #Array #Dynamic_Programming #Breadth_First_Search
# #Algorithm_II_Day_18_Dynamic_Programming #Dynamic_Programming_I_Day_20
# #Level_2_Day_12_Dynamic_Programming #Top_Interview_150_1D_DP #Big_O_Time_O(m*n)_Space_O(amount)
# #2025_07_25_Time_454_ms_(96.33%)_Space_18.19_MB_(69.69%)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                prev = dp[i - coin]
                if prev > 0:
                    if dp[i] == 0:
                        dp[i] = prev + 1
                    else:
                        dp[i] = min(dp[i], prev + 1)
        
        return dp[amount] - 1 if dp[amount] > 0 else -1
