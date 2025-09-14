import unittest
from Solution0172 import Solution

class SolutionTest(unittest.TestCase):
    def test_trailingZeroes(self):
        self.assertEqual(Solution().trailingZeroes(3), 0)

    def test_trailingZeroes2(self):
        self.assertEqual(Solution().trailingZeroes(5), 1)

    def test_trailingZeroes3(self):
        self.assertEqual(Solution().trailingZeroes(0), 0)
