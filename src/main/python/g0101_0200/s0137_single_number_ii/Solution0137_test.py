import unittest
from Solution0137 import Solution

class SolutionTest(unittest.TestCase):
    def test_singleNumber(self):
        self.assertEqual(Solution().singleNumber([2, 2, 3, 2]), 3)

    def test_singleNumber2(self):
        self.assertEqual(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)
