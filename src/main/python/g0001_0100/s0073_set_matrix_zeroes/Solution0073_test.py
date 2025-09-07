import unittest
from Solution0073 import Solution

class SolutionTest(unittest.TestCase):
    def test_setZeroes(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Solution().setZeroes(matrix)
        expected = [[1,0,1],[0,0,0],[1,0,1]]
        self.assertEqual(matrix, expected)

    def test_setZeroes2(self):
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Solution().setZeroes(matrix)
        expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        self.assertEqual(matrix, expected)
