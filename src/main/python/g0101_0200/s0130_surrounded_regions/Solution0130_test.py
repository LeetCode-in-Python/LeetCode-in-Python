import unittest
from Solution0130 import Solution

class SolutionTest(unittest.TestCase):
    def test_solve(self):
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        Solution().solve(board)
        expected = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        self.assertEqual(board, expected)

    def test_solve2(self):
        board = [['X']]
        Solution().solve(board)
        expected = [['X']]
        self.assertEqual(board, expected)
