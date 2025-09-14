import unittest
from Solution0167 import Solution

class SolutionTest(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_twoSum2(self):
        self.assertEqual(Solution().twoSum([2, 3, 4], 6), [1, 3])

    def test_twoSum3(self):
        self.assertEqual(Solution().twoSum([-1, 0], -1), [1, 2])
