import unittest
from Solution0084 import Solution

class SolutionTest(unittest.TestCase):
    def test_largestRectangleArea(self):
        self.assertEqual(Solution().largestRectangleArea([2,1,5,6,2,3]), 10)

    def test_largestRectangleArea2(self):
        self.assertEqual(Solution().largestRectangleArea([2,4]), 4)

    def test_largestRectangleArea3(self):
        self.assertEqual(Solution().largestRectangleArea([1]), 1)
