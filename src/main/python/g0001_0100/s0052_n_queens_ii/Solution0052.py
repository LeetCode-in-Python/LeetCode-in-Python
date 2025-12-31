# #Hard #Backtracking #Top_Interview_150_Backtracking
# #2025_09_20_Time_3_ms_(96.02%)_Space_17.86_MB_(43.80%)

class Solution:
    def totalNQueens(self, n: int) -> int:
        row = [False] * n
        col = [False] * n
        diagonal = [False] * (2 * n - 1)
        anti_diagonal = [False] * (2 * n - 1)
        return self._totalNQueens(n, 0, row, col, diagonal, anti_diagonal)

    def _totalNQueens(self, n, r, row, col, diagonal, anti_diagonal):
        if r == n:
            return 1
        count = 0
        for c in range(n):
            if not row[r] and not col[c] and not diagonal[r + c] and not anti_diagonal[r - c + n - 1]:
                row[r] = col[c] = diagonal[r + c] = anti_diagonal[r - c + n - 1] = True
                count += self._totalNQueens(n, r + 1, row, col, diagonal, anti_diagonal)
                row[r] = col[c] = diagonal[r + c] = anti_diagonal[r - c + n - 1] = False
        return count
