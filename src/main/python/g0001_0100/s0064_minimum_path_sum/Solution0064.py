# #Medium #Top_100_Liked_Questions #Array #Dynamic_Programming #Matrix
# #Dynamic_Programming_I_Day_16 #Udemy_Dynamic_Programming #Top_Interview_150_Multidimensional_DP
# #Big_O_Time_O(m*n)_Space_O(m*n) #2025_07_24_Time_15_ms_(60.38%)_Space_20.01_MB_(64.76%)

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0]*m for _ in range(n)]

        dp[0][0] = grid[0][0]
        for j in range(1,m):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1,n):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, n):
            for j in range(1,m):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        return dp[n-1][m-1]
