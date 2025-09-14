import unittest
from Solution0120 import Solution

class SolutionTest(unittest.TestCase):
    def test_minimumTotal(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        self.assertEqual(Solution().minimumTotal(triangle), 11)

    def test_minimumTotal2(self):
        triangle = [[-10]]
        self.assertEqual(Solution().minimumTotal(triangle), -10)
