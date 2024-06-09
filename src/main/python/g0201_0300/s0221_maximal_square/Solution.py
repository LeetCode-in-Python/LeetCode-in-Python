# #Medium #Array #Dynamic_Programming #Matrix #Dynamic_Programming_I_Day_16
# #Big_O_Time_O(m*n)_Space_O(m*n) #2024_06_09_Time_510_ms_(82.54%)_Space_19.3_MB_(68.21%)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        
        if m == 0 or n == 0:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1])
                    max_side = max(max_side, dp[i + 1][j + 1])

        return max_side * max_side
