import unittest
from Solution0452 import Solution

class SolutionTest(unittest.TestCase):
    def test_findMinArrowShots(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        self.assertEqual(Solution().findMinArrowShots(points), 2)

    def test_findMinArrowShots2(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        self.assertEqual(Solution().findMinArrowShots(points), 4)

    def test_findMinArrowShots3(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual(Solution().findMinArrowShots(points), 2)
