import unittest
from Solution0121 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxProfit(self):
        self.assertEqual(Solution().maxProfit([7,1,5,3,6,4]), 5)

    def test_maxProfit2(self):
        self.assertEqual(Solution().maxProfit([7,6,4,3,1]), 0)

    def test_maxProfit3(self):
        self.assertEqual(Solution().maxProfit([1]), 0)
