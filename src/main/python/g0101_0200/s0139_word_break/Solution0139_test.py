import unittest
from Solution0139 import Solution

class SolutionTest(unittest.TestCase):
    def test_wordBreak(self):
        self.assertTrue(Solution().wordBreak("leetcode", ["leet","code"]))

    def test_wordBreak2(self):
        self.assertTrue(Solution().wordBreak("applepenapple", ["apple","pen"]))

    def test_wordBreak3(self):
        self.assertFalse(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

    def test_wordBreak4(self):
        self.assertTrue(Solution().wordBreak("a", ["a"]))
