import unittest
from Solution0028 import Solution

class SolutionTest(unittest.TestCase):
    def test_strStr(self):
        self.assertEqual(Solution().strStr("hello", "ll"), 2)

    def test_strStr2(self):
        self.assertEqual(Solution().strStr("hello", ""), 0)

    def test_strStr3(self):
        self.assertEqual(Solution().strStr("hello", "oo"), -1)
