import unittest
from Solution0136 import Solution

class SolutionTest(unittest.TestCase):
    def test_singleNumber(self):
        self.assertEqual(Solution().singleNumber([2,2,1]), 1)

    def test_singleNumber2(self):
        self.assertEqual(Solution().singleNumber([4,1,2,1,2]), 4)

    def test_singleNumber3(self):
        self.assertEqual(Solution().singleNumber([1]), 1)
