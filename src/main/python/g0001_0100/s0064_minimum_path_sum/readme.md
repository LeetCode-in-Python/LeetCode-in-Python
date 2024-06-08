64\. Minimum Path Sum

Medium

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

**Input:** grid = [[1,3,1],[1,5,1],[4,2,1]]

**Output:** 7

**Explanation:** Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum. 

**Example 2:**

**Input:** grid = [[1,2,3],[4,5,6]]

**Output:** 12 

**Constraints:**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 200`
*   `0 <= grid[i][j] <= 100`

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `minPathSum` that takes `grid` as an input parameter.
3. Implement the logic to calculate the minimum path sum using dynamic programming.
4. Create a 2D grid of size `m x n` to store the minimum path sum to each cell.
5. Initialize the first row and first column of the grid with cumulative sums.
6. Iterate through the grid starting from the second row and second column.
7. For each cell, update its value to the minimum of the values to its left and above plus the current cell's value.
8. Return the value in the bottom-right cell of the grid, which represents the minimum path sum.

Here's the implementation:

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Create a grid to store the minimum path sum to each cell
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first row and first column
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Calculate the minimum path sum for each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        # Return the minimum path sum in the bottom-right cell
        return dp[m-1][n-1]

# Example usage:
solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
print(solution.minPathSum([[1,2,3],[4,5,6]]))        # Output: 12
```

This implementation uses dynamic programming to efficiently calculate the minimum path sum. It iterates through the grid only once, so the time complexity is O(m * n), where m is the number of rows and n is the number of columns.