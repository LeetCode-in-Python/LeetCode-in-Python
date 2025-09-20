import unittest
from Solution0149 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxPoints(self):
        input_points = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(Solution().maxPoints(input_points), 3)

    def test_maxPoints2(self):
        input_points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        self.assertEqual(Solution().maxPoints(input_points), 4)
