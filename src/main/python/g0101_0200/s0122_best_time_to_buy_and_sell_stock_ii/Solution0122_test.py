import unittest
from Solution0122 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxProfit(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_maxProfit2(self):
        self.assertEqual(Solution().maxProfit([1, 2, 3, 4, 5]), 4)

    def test_maxProfit3(self):
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
