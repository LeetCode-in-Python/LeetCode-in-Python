import unittest
from Solution0150 import Solution

class SolutionTest(unittest.TestCase):
    def test_evalRPN(self):
        self.assertEqual(Solution().evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test_evalRPN2(self):
        self.assertEqual(Solution().evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_evalRPN3(self):
        self.assertEqual(
            Solution().evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22
        )
