import unittest
from Solution0300 import Solution

class SolutionTest(unittest.TestCase):
    def test_lengthOfLIS(self):
        self.assertEqual(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_lengthOfLIS2(self):
        self.assertEqual(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)

    def test_lengthOfLIS3(self):
        self.assertEqual(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)
