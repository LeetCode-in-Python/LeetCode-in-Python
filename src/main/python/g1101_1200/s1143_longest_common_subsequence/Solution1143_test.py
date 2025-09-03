import unittest
from Solution1143 import Solution

import unittest

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestCommonSubsequence(self):
        self.assertEqual(self.solution.longestCommonSubsequence("abcde", "ace"), 3)

    def test_longestCommonSubsequence2(self):
        self.assertEqual(self.solution.longestCommonSubsequence("abc", "abc"), 3)

    def test_longestCommonSubsequence3(self):
        self.assertEqual(self.solution.longestCommonSubsequence("abc", "def"), 0)
