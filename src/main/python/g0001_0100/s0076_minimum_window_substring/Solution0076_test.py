import unittest
from Solution0076 import Solution

class SolutionTest(unittest.TestCase):
    def test_minWindow(self):
        self.assertEqual(Solution().minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_minWindow2(self):
        self.assertEqual(Solution().minWindow("a", "a"), "a")

    def test_minWindow3(self):
        self.assertEqual(Solution().minWindow("a", "aa"), "")
