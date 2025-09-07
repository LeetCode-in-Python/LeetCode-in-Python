import unittest
from Solution0070 import Solution

class SolutionTest(unittest.TestCase):
    def test_climbStairs(self):
        self.assertEqual(Solution().climbStairs(2), 2)

    def test_climbStairs2(self):
        self.assertEqual(Solution().climbStairs(3), 3)

    def test_climbStairs3(self):
        self.assertEqual(Solution().climbStairs(1), 1)
