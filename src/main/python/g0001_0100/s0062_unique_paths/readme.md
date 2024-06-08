62\. Unique Paths

Medium

A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

**Input:** m = 3, n = 7

**Output:** 28 

**Example 2:**

**Input:** m = 3, n = 2

**Output:** 3

**Explanation:**

    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down 

**Example 3:**

**Input:** m = 7, n = 3

**Output:** 28 

**Example 4:**

**Input:** m = 3, n = 3

**Output:** 6 

**Constraints:**

*   `1 <= m, n <= 100`
*   It's guaranteed that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `uniquePaths` that takes `m` and `n` as input parameters.
3. Implement the logic to calculate the number of unique paths using dynamic programming.
4. Create a grid of size `m x n` to store the number of unique paths to each cell.
5. Initialize the first row and first column of the grid to 1, as there is only one way to reach any cell in the first row or column.
6. Iterate through the grid and calculate the number of unique paths to each cell using the formula `grid[i][j] = grid[i-1][j] + grid[i][j-1]`.
7. Return the number of unique paths to the bottom-right corner of the grid (`grid[m-1][n-1]`).

Here's the implementation:

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a grid to store the number of unique paths to each cell
        grid = [[0] * n for _ in range(m)]
        
        # Initialize the first row and first column to 1
        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1
        
        # Calculate the number of unique paths to each cell
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        # Return the number of unique paths to the bottom-right corner
        return grid[m-1][n-1]

# Example usage:
solution = Solution()
print(solution.uniquePaths(3, 7))  # Output: 28
print(solution.uniquePaths(3, 2))  # Output: 3
print(solution.uniquePaths(7, 3))  # Output: 28
print(solution.uniquePaths(3, 3))  # Output: 6
```

This implementation uses dynamic programming to efficiently calculate the number of unique paths. It iterates through the grid only once, so the time complexity is O(m * n), where m is the number of rows and n is the number of columns.