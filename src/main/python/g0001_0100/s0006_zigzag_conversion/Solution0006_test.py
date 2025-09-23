import unittest
from Solution0006 import Solution

class SolutionTest(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_convert2(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
