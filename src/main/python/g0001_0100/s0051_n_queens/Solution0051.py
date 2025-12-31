# #Hard #Top_100_Liked_Questions #Array #Backtracking #Big_O_Time_O(N!)_Space_O(N)
# #2025_07_24_Time_6_ms_(98.12%)_Space_18.42_MB_(15.31%)

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos = [False] * (n + 2 * n - 1 + 2 * n - 1)
        pos2 = [0] * n
        ans = []
        self.helper(n, 0, pos, pos2, ans)
        return ans

    def helper(self, n: int, row: int, pos: List[bool], pos2: List[int], ans: List[List[str]]):
        if row == n:
            self.construct(n, pos2, ans)
            return
        for i in range(n):
            index = n + 2 * n - 1 + n - 1 + i - row
            if pos[i] or pos[n + i + row] or pos[index]:
                continue
            pos[i] = True
            pos[n + i + row] = True
            pos[index] = True
            pos2[row] = i
            self.helper(n, row + 1, pos, pos2, ans)
            pos[i] = False
            pos[n + i + row] = False
            pos[index] = False

    def construct(self, n: int, pos: List[int], ans: List[List[str]]):
        sol = []
        for r in range(n):
            queen_row = ['.'] * n
            queen_row[pos[r]] = 'Q'
            sol.append(''.join(queen_row))
        ans.append(sol)
