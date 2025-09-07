# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Depth_First_Search
# #Breadth_First_Search #Matrix #Union_Find
# #Algorithm_II_Day_6_Breadth_First_Search_Depth_First_Search
# #Graph_Theory_I_Day_1_Matrix_Related_Problems #Level_1_Day_9_Graph/BFS/DFS #Udemy_Graph
# #Top_Interview_150_Graph_General #Big_O_Time_O(M*N)_Space_O(M*N)
# #2025_07_25_Time_234_ms_(82.73%)_Space_19.96_MB_(95.69%)

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
                return
            grid[x][y] = 'x'
            dfs(grid, x + 1, y)
            dfs(grid, x - 1, y)
            dfs(grid, x, y + 1)
            dfs(grid, x, y - 1)
        
        islands = 0
        if grid and grid[0]:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        dfs(grid, i, j)
                        islands += 1
        return islands
