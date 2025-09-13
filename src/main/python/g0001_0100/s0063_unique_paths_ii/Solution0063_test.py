import unittest
from Solution0063 import Solution

class SolutionTest(unittest.TestCase):
    def test_uniquePathsWithObstacles(self):
        obstacle_grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(Solution().uniquePathsWithObstacles(obstacle_grid), 2)

    def test_uniquePathsWithObstacles2(self):
        obstacle_grid = [[0, 1], [0, 0]]
        self.assertEqual(Solution().uniquePathsWithObstacles(obstacle_grid), 1)
