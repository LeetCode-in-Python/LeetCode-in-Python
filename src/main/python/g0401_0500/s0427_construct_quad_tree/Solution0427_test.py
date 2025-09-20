import unittest
from Solution0427 import Solution

class SolutionTest(unittest.TestCase):
    def test_construct(self):
        grid = [[0, 1], [1, 0]]
        result = Solution().construct(grid)
        expected = "[1,0][0,1][1,1][1,1][0,1]"
        self.assertEqual(str(result), expected)

    def test_construct2(self):
        grid = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]
        ]
        result = Solution().construct(grid)
        expected = "[1,0][1,1][1,0][0,1][0,1][1,1][1,1][1,1][0,1]"
        self.assertEqual(str(result), expected)
