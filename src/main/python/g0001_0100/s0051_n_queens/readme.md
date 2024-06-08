51\. N-Queens

Hard

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

**Input:** n = 4

**Output:** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

**Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above 

**Example 2:**

**Input:** n = 1

**Output:** [["Q"]] 

**Constraints:**

*   `1 <= n <= 9`

To solve the N-Queens problem, which involves placing N queens on an N x N chessboard without attacking each other, you can use backtracking. Here are the steps to solve the problem:

### Approach:

1. **Initialize the Chessboard:**
   - Initialize an empty N x N chessboard grid.

2. **Backtracking Function:**
   - Define a backtracking function to recursively explore all possible queen placements.

3. **Base Case:**
   - If all queens are placed (i.e., row index equals N), add the current configuration to the list of solutions.

4. **Try Placing Queen:**
   - For the current row, try placing the queen in each column (0 to N-1).
   - If placing the queen at the current position is safe (i.e., not attacking any other queen), mark the cell as a queen ('Q') and recursively move to the next row.

5. **Backtrack:**
   - After exploring all possibilities from the current position, backtrack by removing the queen from the current position and try the next column.

6. **Return Solutions:**
   - Return the list of all distinct solutions found.

### Python Code:

```python
class Solution:
    def solveNQueens(self, n):
        def is_safe(row, col):
            # Check for queens in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check for queens in the upper-left diagonal
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check for queens in the upper-right diagonal
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtrack(row):
            if row == n:
                solutions.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        backtrack(0)
        return solutions

# Example Usage:
solution = Solution()
print(solution.solveNQueens(4))  # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solution.solveNQueens(1))  # Output: [["Q"]]
```

This code defines a `Solution` class with a `solveNQueens` method to find all distinct solutions to the N-Queens puzzle. The example usage demonstrates how to create an instance of the `Solution` class and call the `solveNQueens` method with different values of `n`.