import unittest
from Solution0026 import Solution

class SolutionTest(unittest.TestCase):
    def test_removeDuplicates(self):
        nums = [1, 1, 2]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_removeDuplicates2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0,1,2,3,4,])
