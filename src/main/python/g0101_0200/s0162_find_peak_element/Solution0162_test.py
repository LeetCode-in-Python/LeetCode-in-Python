import unittest
from Solution0162 import Solution

class SolutionTest(unittest.TestCase):
    def test_findPeakElement(self):
        self.assertEqual(Solution().findPeakElement([1, 2, 3, 1]), 2)

    def test_findPeakElement2(self):
        self.assertEqual(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]), 5)
