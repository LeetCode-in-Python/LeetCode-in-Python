import unittest
from Solution0097 import Solution

class SolutionTest(unittest.TestCase):
    def test_isInterleave(self):
        self.assertTrue(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_isInterleave2(self):
        self.assertFalse(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_isInterleave3(self):
        self.assertTrue(Solution().isInterleave("", "", ""))
