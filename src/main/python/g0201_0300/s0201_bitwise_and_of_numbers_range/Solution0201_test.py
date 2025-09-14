import unittest
from Solution0201 import Solution

class SolutionTest(unittest.TestCase):
    def test_rangeBitwiseAnd(self):
        self.assertEqual(Solution().rangeBitwiseAnd(5, 7), 4)

    def test_rangeBitwiseAnd2(self):
        self.assertEqual(Solution().rangeBitwiseAnd(0, 0), 0)

    def test_rangeBitwiseAnd3(self):
        self.assertEqual(Solution().rangeBitwiseAnd(1, 2147483647), 0)

