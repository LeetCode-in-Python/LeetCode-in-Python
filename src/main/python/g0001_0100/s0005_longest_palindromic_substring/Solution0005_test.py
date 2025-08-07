import unittest
from Solution0005 import Solution

class SolutionTest(unittest.TestCase):
    def test_longestPalindrome(self):
        self.assertEqual(Solution().longestPalindrome("babad"), "bab")

    def test_longestPalindrome2(self):
        self.assertEqual(Solution().longestPalindrome("cbbd"), "bb")
