import unittest
from Solution0338 import Solution

class SolutionTest(unittest.TestCase):
    def test_countBits(self):
        self.assertEqual(Solution().countBits(2), [0, 1, 1])

    def test_countBits2(self):
        self.assertEqual(Solution().countBits(5), [0, 1, 1, 2, 1, 2])
