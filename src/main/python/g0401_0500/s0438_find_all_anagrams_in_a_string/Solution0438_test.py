import unittest
from Solution0438 import Solution

class SolutionTest(unittest.TestCase):
    def test_findAnagrams(self):
        self.assertEqual(Solution().findAnagrams("cbaebabacd", "abc"), [0, 6])

    def test_findAnagrams2(self):
        self.assertEqual(Solution().findAnagrams("abab", "ab"), [0, 1, 2])
