import unittest
from Solution0035 import Solution

class SolutionTest(unittest.TestCase):
    def test_searchInsert(self):
        self.assertEqual(Solution().searchInsert([1,3,5,6], 5), 2)

    def test_searchInsert2(self):
        self.assertEqual(Solution().searchInsert([1,3,5,6], 2), 1)

    def test_searchInsert3(self):
        self.assertEqual(Solution().searchInsert([1,3,5,6], 7), 4)

    def test_searchInsert4(self):
        self.assertEqual(Solution().searchInsert([1,3,5,6], 0), 0)
