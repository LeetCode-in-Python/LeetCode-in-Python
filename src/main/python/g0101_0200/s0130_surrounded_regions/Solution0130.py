# #Medium #Top_Interview_Questions #Array #Depth_First_Search #Breadth_First_Search #Matrix
# #Union_Find #Algorithm_II_Day_8_Breadth_First_Search_Depth_First_Search
# #Top_Interview_150_Graph_General #2025_09_14_Time_3_ms_(86.86%)_Space_21.58_MB_(88.48%)

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Edge case, empty grid
        if not board:
            return
        # Traverse first and last rows (boundaries)
        for i in range(len(board[0])):
            # first row
            if board[0][i] == 'O':
                # It will convert O and all it's touching O's to #
                self._dfs(board, 0, i)
            # last row
            if board[len(board) - 1][i] == 'O':
                # Converts O's to #'s (same thing as above)
                self._dfs(board, len(board) - 1, i)
        # Traverse first and last Column (boundaries)
        for i in range(len(board)):
            # first Column
            if board[i][0] == 'O':
                # Converts O's to #'s
                self._dfs(board, i, 0)
            # last Column
            if board[i][len(board[0]) - 1] == 'O':
                # Converts O's to #'s
                self._dfs(board, i, len(board[0]) - 1)
        # Traverse through entire matrix
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    # Convert O's to X's
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    # Convert #'s to O's
                    board[i][j] = 'O'

    def _dfs(self, board: List[List[str]], row: int, column: int):
        if (row < 0 or row >= len(board) or column < 0 or 
            column >= len(board[0]) or board[row][column] != 'O'):
            return
        board[row][column] = '#'
        self._dfs(board, row + 1, column)
        self._dfs(board, row - 1, column)
        self._dfs(board, row, column + 1)
        self._dfs(board, row, column - 1)
