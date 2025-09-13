import unittest
from Solution0071 import Solution

class SolutionTest(unittest.TestCase):
    def test_simplifyPath(self):
        self.assertEqual(Solution().simplifyPath("/home/"), "/home")

    def test_simplifyPath2(self):
        self.assertEqual(Solution().simplifyPath("/../"), "/")

    def test_simplifyPath3(self):
        self.assertEqual(Solution().simplifyPath("/home//foo/"), "/home/foo")
