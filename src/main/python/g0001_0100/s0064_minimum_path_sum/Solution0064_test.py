import unittest
from Solution0064 import Solution

class SolutionTest(unittest.TestCase):
    def test_minPathSum(self):
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(Solution().minPathSum(grid), 7)

    def test_minPathSum2(self):
        grid = [[1,2,3],[4,5,6]]
        self.assertEqual(Solution().minPathSum(grid), 12)

    def test_minPathSum3(self):
        grid = [[1,2],[1,1]]
        self.assertEqual(Solution().minPathSum(grid), 3)
