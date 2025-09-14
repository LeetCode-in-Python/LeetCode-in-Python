import unittest
from Solution0123 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxProfit(self):
        self.assertEqual(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 6)

    def test_maxProfit2(self):
        self.assertEqual(Solution().maxProfit([1, 2, 3, 4, 5]), 4)

    def test_maxProfit3(self):
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
