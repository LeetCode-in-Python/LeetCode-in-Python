import unittest
from Solution0012 import Solution

class SolutionTest(unittest.TestCase):
    def test_intToRoman(self):
        self.assertEqual(Solution().intToRoman(3), "III")

    def test_intToRoman2(self):
        self.assertEqual(Solution().intToRoman(4), "IV")

    def test_intToRoman3(self):
        self.assertEqual(Solution().intToRoman(9), "IX")

    def test_intToRoman4(self):
        self.assertEqual(Solution().intToRoman(58), "LVIII")

    def test_intToRoman5(self):
        self.assertEqual(Solution().intToRoman(1994), "MCMXCIV")


