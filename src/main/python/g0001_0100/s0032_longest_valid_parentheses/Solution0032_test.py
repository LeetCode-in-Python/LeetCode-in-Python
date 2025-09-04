import unittest
from Solution0032 import Solution

class SolutionTest(unittest.TestCase):
    def test_longestValidParentheses(self):
        self.assertEqual(Solution().longestValidParentheses("(()"), 2)

    def test_longestValidParentheses2(self):
        self.assertEqual(Solution().longestValidParentheses(")()())"), 4)
