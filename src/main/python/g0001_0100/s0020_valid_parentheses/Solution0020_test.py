import unittest
from Solution0020 import Solution


class SolutionTest(unittest.TestCase):
    def test_isValid(self):
        self.assertTrue(Solution().isValid("()"))

    def test_isValid2(self):
        self.assertTrue(Solution().isValid("()[]{}"))

    def test_isValid3(self):
        self.assertFalse(Solution().isValid("(]"))

    def test_isValid4(self):
        self.assertFalse(Solution().isValid("([)]"))

    def test_isValid5(self):
        self.assertTrue(Solution().isValid("{[]}")) 