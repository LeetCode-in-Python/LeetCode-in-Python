import unittest
from Solution0013 import Solution

class SolutionTest(unittest.TestCase):
    def test_romanToInt(self):
        self.assertEqual(Solution().romanToInt("III"), 3)

    def test_romanToInt2(self):
        self.assertEqual(Solution().romanToInt("IV"), 4)

    def test_romanToInt3(self):
        self.assertEqual(Solution().romanToInt("IX"), 9)

    def test_romanToInt4(self):
        self.assertEqual(Solution().romanToInt("LVIII"), 58)

    def test_romanToInt5(self):
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)
