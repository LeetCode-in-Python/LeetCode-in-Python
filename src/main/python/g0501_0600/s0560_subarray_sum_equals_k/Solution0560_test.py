import unittest
from Solution0560 import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subarraySum(self):
        self.assertEqual(self.solution.subarraySum([1, 1, 1], 2), 2)

    def test_subarraySum2(self):
        self.assertEqual(self.solution.subarraySum([1, 2, 3], 3), 2)
