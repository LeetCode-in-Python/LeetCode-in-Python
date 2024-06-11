200\. Number of Islands

Medium

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

**Input:**

    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]

**Output:** 1 

**Example 2:**

**Input:**

    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]

**Output:** 3 

**Constraints:**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 300`
*   `grid[i][j]` is `'0'` or `'1'`.

To solve the Number of Islands problem, we can utilize Depth-First Search (DFS) to traverse the grid and identify the islands. Here's a step-by-step approach to solve this problem:

1. **Define DFS Function**:
   - Define a DFS function to traverse the grid recursively.
   - This function will mark visited cells as `'0'` to avoid revisiting them.
   - It will explore adjacent cells (up, down, left, right) and continue DFS traversal if the adjacent cell is land (`'1'`).

2. **Iterate Through Grid**:
   - Iterate through each cell in the grid.
   
3. **Count Islands**:
   - For each cell with land (`'1'`), call the DFS function to explore the island.
   - Increment the count of islands by 1 after each DFS traversal.

4. **Return Count**:
   - After traversing the entire grid, return the count of islands.

Let's implement this approach:

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Mark the current cell as visited
            # Explore adjacent cells
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        
        if not grid:
            return 0
        
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid, i, j)
        
        return num_islands
```

This solution efficiently counts the number of islands in the given grid by performing DFS traversal on each unvisited land cell. It has a time complexity of O(M * N), where M is the number of rows and N is the number of columns in the grid.