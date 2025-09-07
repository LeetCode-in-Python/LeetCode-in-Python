import unittest
from Solution0075 import Solution

class SolutionTest(unittest.TestCase):
    def test_sortColors(self):
        nums = [2,0,2,1,1,0]
        Solution().sortColors(nums)
        self.assertEqual(nums, [0,0,1,1,2,2])

    def test_sortColors2(self):
        nums = [2,0,1]
        Solution().sortColors(nums)
        self.assertEqual(nums, [0,1,2])

    def test_sortColors3(self):
        nums = [0]
        Solution().sortColors(nums)
        self.assertEqual(nums, [0])
