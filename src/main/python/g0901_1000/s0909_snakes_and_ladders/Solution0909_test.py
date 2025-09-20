import unittest
from Solution0909 import Solution

class SolutionTest(unittest.TestCase):
    def test_snakesAndLadders(self):
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1]
        ]
        self.assertEqual(Solution().snakesAndLadders(board), 4)

    def test_snakesAndLadders2(self):
        board = [[-1, -1], [-1, 3]]
        self.assertEqual(Solution().snakesAndLadders(board), 1)
