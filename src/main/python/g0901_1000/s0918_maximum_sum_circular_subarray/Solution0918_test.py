import unittest
from Solution0918 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxSubarraySumCircular(self):
        self.assertEqual(Solution().maxSubarraySumCircular([1, -2, 3, -2]), 3)

    def test_maxSubarraySumCircular2(self):
        self.assertEqual(Solution().maxSubarraySumCircular([5, -3, 5]), 10)

    def test_maxSubarraySumCircular3(self):
        self.assertEqual(Solution().maxSubarraySumCircular([-3, -2, -3]), -2)
