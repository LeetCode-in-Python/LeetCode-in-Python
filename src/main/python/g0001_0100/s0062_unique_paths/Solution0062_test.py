import unittest
from Solution0062 import Solution

class SolutionTest(unittest.TestCase):
    def test_uniquePaths(self):
        self.assertEqual(Solution().uniquePaths(3, 7), 28)

    def test_uniquePaths2(self):
        self.assertEqual(Solution().uniquePaths(3, 2), 3)

    def test_uniquePaths3(self):
        self.assertEqual(Solution().uniquePaths(1, 1), 1)
