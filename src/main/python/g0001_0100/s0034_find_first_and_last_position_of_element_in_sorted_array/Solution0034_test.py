import unittest
from Solution0034 import Solution

class SolutionTest(unittest.TestCase):
    def test_searchRange(self):
        self.assertEqual(Solution().searchRange([5,7,7,8,8,10], 8), [3, 4])

    def test_searchRange2(self):
        self.assertEqual(Solution().searchRange([5,7,7,8,8,10], 6), [-1, -1])

    def test_searchRange3(self):
        self.assertEqual(Solution().searchRange([], 0), [-1, -1])
