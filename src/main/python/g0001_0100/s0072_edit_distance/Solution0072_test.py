import unittest
from Solution0072 import Solution

class SolutionTest(unittest.TestCase):
    def test_minDistance(self):
        self.assertEqual(Solution().minDistance("horse", "ros"), 3)

    def test_minDistance2(self):
        self.assertEqual(Solution().minDistance("intention", "execution"), 5)

    def test_minDistance3(self):
        self.assertEqual(Solution().minDistance("", "a"), 1)
