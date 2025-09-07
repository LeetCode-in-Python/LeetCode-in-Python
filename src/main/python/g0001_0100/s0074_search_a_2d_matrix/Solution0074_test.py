import unittest
from Solution0074 import Solution

class SolutionTest(unittest.TestCase):
    def test_searchMatrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(Solution().searchMatrix(matrix, 3))

    def test_searchMatrix2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertFalse(Solution().searchMatrix(matrix, 13))
