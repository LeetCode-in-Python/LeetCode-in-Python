import unittest
from Solution0224 import Solution

class SolutionTest(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(Solution().calculate("1 + 1"), 2)

    def test_calculate2(self):
        self.assertEqual(Solution().calculate(" 2-1 + 2 "), 3)

    def test_calculate3(self):
        self.assertEqual(Solution().calculate("(1+(4+5+2)-3)+(6+8)"), 23)
