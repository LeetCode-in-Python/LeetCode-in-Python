import unittest
from Solution0189 import Solution

class SolutionTest(unittest.TestCase):
    def test_rotate(self):
        nums = [1,2,3,4,5,6,7]
        Solution().rotate(nums, 3)
        self.assertEqual(nums, [5,6,7,1,2,3,4])

    def test_rotate2(self):
        nums = [-1,-100,3,99]
        Solution().rotate(nums, 2)
        self.assertEqual(nums, [3,99,-1,-100])

    def test_rotate3(self):
        nums = [1,2]
        Solution().rotate(nums, 1)
        self.assertEqual(nums, [2,1])

    def test_rotate4(self):
        nums = [1,2,3,4,5,6]
        Solution().rotate(nums, 2)
        self.assertEqual(nums, [5,6,1,2,3,4])
