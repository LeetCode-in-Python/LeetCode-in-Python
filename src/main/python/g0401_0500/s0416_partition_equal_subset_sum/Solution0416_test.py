import unittest
from Solution0416 import Solution

class SolutionTest(unittest.TestCase):
    def test_canPartition(self):
        self.assertEqual(Solution().canPartition([1, 5, 11, 5]), True)

    def test_canPartition2(self):
        self.assertEqual(Solution().canPartition([1, 2, 3, 5]), False)
