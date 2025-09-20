import unittest
from Solution0052 import Solution

class SolutionTest(unittest.TestCase):
    def test_totalNQueens(self):
        self.assertEqual(Solution().totalNQueens(4), 2)

    def test_totalNQueens2(self):
        self.assertEqual(Solution().totalNQueens(1), 1)
