import unittest
from Solution0647 import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countSubstrings(self):
        self.assertEqual(self.solution.countSubstrings("abc"), 3)

    def test_countSubstrings2(self):
        self.assertEqual(self.solution.countSubstrings("aaa"), 6)
