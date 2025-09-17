import unittest
from Solution0289 import Solution

class SolutionTest(unittest.TestCase):
    def test_gameOfLife(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        Solution().gameOfLife(board)
        self.assertEqual(board, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])

    def test_gameOfLife2(self):
        board = [[1, 1], [1, 0]]
        Solution().gameOfLife(board)
        self.assertEqual(board, [[1, 1], [1, 1]])
