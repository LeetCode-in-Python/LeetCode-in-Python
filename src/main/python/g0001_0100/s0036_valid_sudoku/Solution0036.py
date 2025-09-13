# #Medium #Top_Interview_Questions #Array #Hash_Table #Matrix #Data_Structure_I_Day_5_Array
# #Top_Interview_150_Matrix #2025_09_13_Time_5_ms_(72.85%)_Space_12.40_MB_(54.10%)

from typing import List

class Solution:
    def __init__(self):
        self.j1 = 0
        self.i1 = [0] * 9
        self.b1 = [0] * 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                res = self._checkValid(board, i, j)
                if not res:
                    return False
        return True

    def _checkValid(self, board: List[List[str]], i: int, j: int) -> bool:
        if j == 0:
            self.j1 = 0
        if board[i][j] == '.':
            return True
        val = int(board[i][j])
        if self.j1 == (self.j1 | (1 << (val - 1))):
            return False
        self.j1 |= 1 << (val - 1)
        if self.i1[j] == (self.i1[j] | (1 << (val - 1))):
            return False
        self.i1[j] |= 1 << (val - 1)
        b = (i // 3) * 3 + j // 3
        if self.b1[b] == (self.b1[b] | (1 << (val - 1))):
            return False
        self.b1[b] |= 1 << (val - 1)
        return True
