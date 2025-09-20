import unittest
from Solution0392 import Solution

class SolutionTest(unittest.TestCase):
    def test_isSubsequence(self):
        self.assertTrue(Solution().isSubsequence("abc", "ahbgdc"))

    def test_isSubsequence2(self):
        self.assertFalse(Solution().isSubsequence("axc", "ahbgdc"))
