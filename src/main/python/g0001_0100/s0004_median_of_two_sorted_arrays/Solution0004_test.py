import unittest
from Solution0004 import Solution

class SolutionTest(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        self.assertEqual(
            Solution().findMedianSortedArrays([1, 3], [2]),
            2.0
        )

    def test_findMedianSortedArrays2(self):
        self.assertEqual(
            Solution().findMedianSortedArrays([1, 2], [3, 4]),
            2.5
        )
