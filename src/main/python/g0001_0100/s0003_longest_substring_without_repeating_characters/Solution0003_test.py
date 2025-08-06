import unittest
from Solution0003 import Solution

class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)

    def test_lengthOfLongestSubstring2(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)

    def test_lengthOfLongestSubstring3(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)
