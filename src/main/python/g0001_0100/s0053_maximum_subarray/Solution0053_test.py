import unittest
from Solution0053 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxSubArray(self):
        self.assertEqual(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test_maxSubArray2(self):
        self.assertEqual(Solution().maxSubArray([1]), 1)

    def test_maxSubArray3(self):
        self.assertEqual(Solution().maxSubArray([5,4,-1,7,8]), 23)
