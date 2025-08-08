import unittest
from Solution0011 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxArea(self):
        self.assertEqual(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_maxArea2(self):
        self.assertEqual(Solution().maxArea([1, 1]), 1)
