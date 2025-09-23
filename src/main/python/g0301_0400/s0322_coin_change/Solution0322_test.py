import unittest
from Solution0322 import Solution

class SolutionTest(unittest.TestCase):
    def test_coinChange(self):
        self.assertEqual(Solution().coinChange([1, 2, 5], 11), 3)

    def test_coinChange2(self):
        self.assertEqual(Solution().coinChange([2], 3), -1)

    def test_coinChange3(self):
        self.assertEqual(Solution().coinChange([1], 0), 0)
