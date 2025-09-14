import unittest
from Solution0151 import Solution


class SolutionTest(unittest.TestCase):
    def test_reverseWords(self):
        self.assertEqual(Solution().reverseWords("the sky is blue"), "blue is sky the")

    def test_reverseWords2(self):
        self.assertEqual(Solution().reverseWords("  hello world  "), "world hello")

    def test_reverseWords3(self):
        self.assertEqual(Solution().reverseWords("a good   example"), "example good a")
