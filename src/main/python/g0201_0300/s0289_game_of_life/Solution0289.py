# #Medium #Array #Matrix #Simulation #Top_Interview_150_Matrix
# #2025_09_17_Time_0_ms_(100.00%)_Space_17.73_MB_(75.41%)

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0]) if m > 0 else 0
        for i in range(m):
            for j in range(n):
                lives = self._lives(board, i, j, m, n)
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and (lives == 2 or lives == 3):
                    board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

    def _lives(self, board: List[List[int]], i: int, j: int, m: int, n: int) -> int:
        lives = 0
        for r in range(max(0, i - 1), min(m - 1, i + 1) + 1):
            for c in range(max(0, j - 1), min(n - 1, j + 1) + 1):
                lives += board[r][c] & 1
        lives -= board[i][j] & 1
        return lives
