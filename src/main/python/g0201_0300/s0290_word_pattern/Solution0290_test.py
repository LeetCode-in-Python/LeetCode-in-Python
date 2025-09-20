import unittest
from Solution0290 import Solution

class SolutionTest(unittest.TestCase):
    def test_wordPattern(self):
        self.assertTrue(Solution().wordPattern("abba", "dog cat cat dog"))

    def test_wordPattern2(self):
        self.assertFalse(Solution().wordPattern("abba", "dog cat cat fish"))

    def test_wordPattern3(self):
        self.assertFalse(Solution().wordPattern("aaaa", "dog cat cat dog"))

    def test_wordPattern4(self):
        self.assertFalse(Solution().wordPattern("abba", "dog dog dog dog"))
