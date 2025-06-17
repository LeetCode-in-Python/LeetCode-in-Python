# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Dynamic_Programming #Math
# #Combinatorics #LeetCode_75_DP/Multidimensional #Algorithm_II_Day_13_Dynamic_Programming
# #Dynamic_Programming_I_Day_15 #Level_1_Day_11_Dynamic_Programming
# #Big_O_Time_O(m*n)_Space_O(m*n) #2024_06_08_Time_24_ms_(98.19%)_Space_16.4_MB_(78.68%)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
       
