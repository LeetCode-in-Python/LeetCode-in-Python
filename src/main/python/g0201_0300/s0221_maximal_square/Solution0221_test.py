import unittest
from Solution0221 import Solution

class SolutionTest(unittest.TestCase):
    def test_maximalSquare(self):
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        self.assertEqual(Solution().maximalSquare(matrix), 4)

    def test_maximalSquare2(self):
        matrix = [["0","1"],["1","0"]]
        self.assertEqual(Solution().maximalSquare(matrix), 1)

    def test_maximalSquare3(self):
        matrix = [["0"]]
        self.assertEqual(Solution().maximalSquare(matrix), 0)
