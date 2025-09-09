import unittest
from Solution0027 import Solution

class SolutionTest(unittest.TestCase):
    def test_removeElement(self):
        nums = [3,2,2,3]
        k = Solution().removeElement(nums, 3)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2,2])

    def test_removeElement2(self):
        nums = [0,1,2,2,3,0,4,2]
        k = Solution().removeElement(nums, 2)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0,0,1,3,4])
