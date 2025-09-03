import unittest
from Solution0022 import Solution

class SolutionTest(unittest.TestCase):
    def test_generateParenthesis(self):
        self.assertEqual(
            Solution().generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )

    def test_generateParenthesis2(self):
        self.assertEqual(Solution().generateParenthesis(1), ["()"])
