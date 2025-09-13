# #Medium #Array #Dynamic_Programming #Matrix #Dynamic_Programming_I_Day_15
# #Top_Interview_150_Multidimensional_DP #2025_09_13_Time_0_ms_(100.00%)_Space_12.44_MB_(66.99%)

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # if start point has obstacle, there's no path
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = obstacleGrid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[m - 1][n - 1]
