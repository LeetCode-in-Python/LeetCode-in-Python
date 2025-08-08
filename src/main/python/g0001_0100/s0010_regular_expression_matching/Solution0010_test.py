import unittest
from Solution0010 import Solution

class SolutionTest(unittest.TestCase):
    def test_isMatch(self):
        self.assertEqual(Solution().isMatch("aa", "a"), False)

    def test_isMatch2(self):
        self.assertEqual(Solution().isMatch("aa", "a*"), True)

    def test_isMatch3(self):
        self.assertEqual(Solution().isMatch("ab", ".*"), True)

    def test_isMatch4(self):
        self.assertEqual(Solution().isMatch("aab", "c*a*b"), True)

    def test_isMatch5(self):
        self.assertEqual(Solution().isMatch("mississippi", "mis*is*p*."), False)
