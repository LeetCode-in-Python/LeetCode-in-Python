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

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `exist` that takes `board` and `word` as input parameters.
3. Implement an algorithm to search for the word in the grid `board`.
4. Use a backtracking approach to explore all possible paths in the grid to find the word.
5. Create a recursive function named `search` that takes `row`, `col`, `index` (current character index in the word), and `visited` (a set of visited cells) as parameters.
6. Base case: If `index` is equal to the length of the word, return True (word found).
7. If the current cell (`board[row][col]`) is not equal to the character at index `index` of the word or the cell is already visited, return False.
8. Mark the current cell as visited by adding `(row, col)` to the set `visited`.
9. Recursively call `search` with the neighboring cells (up, down, left, right) and increment `index` by 1.
10. If any of the recursive calls return True, return True.
11. After exploring all possible paths from the current cell, backtrack by removing `(row, col)` from `visited`.
12. Return False if no path from the current cell leads to finding the word.
13. Iterate through each cell in the grid and call the `search` function with the starting position and index 0.
14. Return the result of the `search` function.

Here's the implementation:

```python
class Solution:
    def exist(self, board, word):
        def search(row, col, index, visited):
            if index == len(word):
                return True
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) \
                    or board[row][col] != word[index] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            if search(row - 1, col, index + 1, visited) \
                    or search(row + 1, col, index + 1, visited) \
                    or search(row, col - 1, index + 1, visited) \
                    or search(row, col + 1, index + 1, visited):
                return True
            
            visited.remove((row, col))
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if search(row, col, 0, set()):
                    return True
        
        return False

# Example usage:
solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(solution.exist(board, "ABCCED"))  # Output: True
print(solution.exist(board, "SEE"))     # Output: True
print(solution.exist(board, "ABCB"))    # Output: False
```

This solution explores all possible paths in the grid to find the word using backtracking. It efficiently searches for the word, and the time complexity depends on the size of the grid and the length of the word.