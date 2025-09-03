import unittest
from Solution0015 import Solution


class SolutionTest(unittest.TestCase):
    def test_threeSum(self):
        self.assertEqual(Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_threeSum2(self):
        self.assertEqual(Solution().threeSum([]), [])

    def test_threeSum3(self):
        self.assertEqual(Solution().threeSum([0]), []) 