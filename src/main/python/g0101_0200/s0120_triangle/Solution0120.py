# #Medium #Array #Dynamic_Programming #Algorithm_I_Day_12_Dynamic_Programming
# #Dynamic_Programming_I_Day_13 #Udemy_Dynamic_Programming #Top_Interview_150_Multidimensional_DP
# #2025_09_14_Time_0_ms_(100.00%)_Space_18.71_MB_(81.95%)

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # create a 1D array, copy last elements
        # iterate reverse last - 1
        n = len(triangle)
        dp = []
        for num in triangle[-1]:
            dp.append(num)
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
