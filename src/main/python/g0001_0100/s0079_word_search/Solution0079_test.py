import unittest
from Solution0079 import Solution

class SolutionTest(unittest.TestCase):
    def test_exist(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertTrue(Solution().exist(board, "ABCCED"))

    def test_exist2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertTrue(Solution().exist(board, "SEE"))

    def test_exist3(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertFalse(Solution().exist(board, "ABCB"))
