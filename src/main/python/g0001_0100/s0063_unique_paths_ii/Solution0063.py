# #Medium #Array #Dynamic_Programming #Matrix #Dynamic_Programming_I_Day_15
# #Top_Interview_150_Multidimensional_DP #2025_09_13_Time_0_ms_(100.00%)_Space_12.44_MB_(66.99%)

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        # if start point has obstacle, there's no path
        if obstacle_grid[0][0] == 1:
            return 0
        obstacle_grid[0][0] = 1
        m = len(obstacle_grid)
        n = len(obstacle_grid[0])
        for i in range(1, m):
            if obstacle_grid[i][0] == 1:
                obstacle_grid[i][0] = 0
            else:
                obstacle_grid[i][0] = obstacle_grid[i - 1][0]
        for j in range(1, n):
            if obstacle_grid[0][j] == 1:
                obstacle_grid[0][j] = 0
            else:
                obstacle_grid[0][j] = obstacle_grid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacle_grid[i][j] == 1:
                    obstacle_grid[i][j] = 0
                else:
                    obstacle_grid[i][j] = obstacle_grid[i - 1][j] + obstacle_grid[i][j - 1]
        return obstacle_grid[m - 1][n - 1]
