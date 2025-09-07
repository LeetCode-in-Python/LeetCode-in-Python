import unittest
from Solution0153 import Solution

class SolutionTest(unittest.TestCase):
    def test_findMin(self):
        self.assertEqual(Solution().findMin([3,4,5,1,2]), 1)

    def test_findMin2(self):
        self.assertEqual(Solution().findMin([4,5,6,7,0,1,2]), 0)

    def test_findMin3(self):
        self.assertEqual(Solution().findMin([11,13,15,17]), 11)

    def test_findMin4(self):
        self.assertEqual(Solution().findMin([1]), 1)
