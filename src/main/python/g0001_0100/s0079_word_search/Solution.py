# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Matrix #Backtracking
# #Algorithm_II_Day_11_Recursion_Backtracking #Big_O_Time_O(4^(m*n))_Space_O(m*n)
# #2024_06_09_Time_619_ms_(95.31%)_Space_16.6_MB_(20.49%)

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

