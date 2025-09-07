import unittest
from Solution0096 import Solution

class SolutionTest(unittest.TestCase):
    def test_numTrees(self):
        self.assertEqual(Solution().numTrees(3), 5)

    def test_numTrees2(self):
        self.assertEqual(Solution().numTrees(1), 1)

    def test_numTrees3(self):
        self.assertEqual(Solution().numTrees(2), 2)
