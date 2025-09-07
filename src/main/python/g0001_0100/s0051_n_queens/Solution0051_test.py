import unittest
from Solution0051 import Solution

def sort_nested(lists):
    return sorted(lists)

class SolutionTest(unittest.TestCase):
    def test_solveNQueens(self):
        res = Solution().solveNQueens(4)
        expected = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_solveNQueens2(self):
        res = Solution().solveNQueens(1)
        expected = [["Q"]]
        self.assertEqual(sort_nested(res), sort_nested(expected))
