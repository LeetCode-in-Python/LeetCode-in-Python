import unittest
from Solution0001 import Solution

class SolutionTest(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_twoSum2(self):
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])

    def test_twoSum3(self):
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])

    def test_twoSum4(self):
        self.assertEqual(Solution().twoSum([3, 3], 7), [-1, -1])
