# #Medium #Top_100_Liked_Questions #String #Dynamic_Programming #LeetCode_75_DP/Multidimensional
# #Algorithm_II_Day_17_Dynamic_Programming #Dynamic_Programming_I_Day_19
# #Udemy_Dynamic_Programming #Big_O_Time_O(n*m)_Space_O(n*m)
# #2024_06_07_Time_452_ms_(81.00%)_Space_41.6_MB_(77.76%)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]
