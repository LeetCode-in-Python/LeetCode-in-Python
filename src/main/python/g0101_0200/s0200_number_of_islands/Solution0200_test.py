import unittest
from Solution0200 import Solution

class SolutionTest(unittest.TestCase):
    def test_numIslands(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(Solution().numIslands(grid), 1)

    def test_numIslands2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(Solution().numIslands(grid), 3)
