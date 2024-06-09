79\. Word Search

Medium

Given an `m x n` grid of characters `board` and a string `word`, return `true` _if_ `word` _exists in the grid_.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

**Output:** true 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"

**Output:** true 

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"

**Output:** false 

**Constraints:**

*   `m == board.length`
*   `n = board[i].length`
*   `1 <= m, n <= 6`
*   `1 <= word.length <= 15`
*   `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

To solve the "Word Search" problem in Python with the Solution class, follow these steps:

1. Define a method `exist` in the `Solution` class that takes a 2D character array `board` and a string `word` as input and returns `true` if the `word` exists in the `board`.
2. Implement a backtracking algorithm to search for the `word` in the `board`.
3. Iterate through each cell in the `board`:
   - For each cell, call a recursive helper function `search` to check if the `word` can be found starting from that cell.
   - If `search` returns `true`, return `true` immediately.
4. Define the `search` method to perform the recursive backtracking:
   - Check if the current cell is out of bounds or if the current character in the `board` does not match the corresponding character in the `word`.
   - If any of the conditions are met, return `false`.
   - Mark the current cell as visited by changing its value to a special character (e.g., `#`) to avoid revisiting it.
   - Recursively call `search` on neighboring cells (up, down, left, right) with the next character in the `word`.
   - After exploring all possible paths from the current cell, backtrack by restoring the original value of the current cell.
5. If the `search` method reaches the end of the `word`, return `true`.
6. If no match is found after exploring all cells, return `false`.

Here's the implementation of the `exist` method in Python:

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        p = len(word)

        if p > n * m:
            return False

        def is_sub(board, word):
            c = Counter()
            for line in board:
                c.update(line)
            return Counter(word) <= c
        
        if not is_sub(board, word):
            return False

        def rec(i, j, k, visited):
            if k == p:
                return True

            for ii, jj in ((i - 1, j),
                           (i + 1, j),
                           (i, j - 1),
                           (i, j + 1)):
                if (
                    0 <= ii < n
                    and 0 <= jj < m
                    and (ii, jj) not in visited
                    and word[k] == board[ii][jj]
                ):
                    visited.add((ii, jj))
                    if rec(ii, jj, k + 1, visited):
                        return True
                    visited.remove((ii, jj))
            return False

        for i, line in enumerate(board):
            for j, elem in enumerate(line):
                if elem == word[0] and rec(i, j, 1, {(i, j)}):
                    return True
        return False

# Example usage:
# sol = Solution()
# board = [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]
# word = "ABCCED"
# print(sol.exist(board, word))  # Output should be True

```

This implementation uses backtracking to search for the word in the board, with a time complexity of O(M * N * 4^L), where M and N are the dimensions of the board and L is the length of the word.