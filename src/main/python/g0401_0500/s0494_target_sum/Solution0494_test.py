import unittest
from Solution0494 import Solution

class SolutionTest(unittest.TestCase):
    def test_findTargetSumWays(self):
        self.assertEqual(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_findTargetSumWays2(self):
        self.assertEqual(Solution().findTargetSumWays([1], 1), 1)
