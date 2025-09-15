import unittest
from Solution0188 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxProfit(self):
        self.assertEqual(Solution().maxProfit(2, [2, 4, 1]), 2)

    def test_maxProfit2(self):
        self.assertEqual(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]), 7)
