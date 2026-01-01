import unittest
from Solution0416 import Solution

class SolutionTest(unittest.TestCase):
    def test_canPartition(self):
        self.assertTrue(Solution().canPartition([1, 5, 11, 5]))

    def test_canPartition2(self):
        self.assertFalse(Solution().canPartition([1, 2, 3, 5]))
