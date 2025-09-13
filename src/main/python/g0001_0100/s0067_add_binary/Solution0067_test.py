import unittest
from Solution0067 import Solution

class SolutionTest(unittest.TestCase):
    def test_addBinary(self):
        self.assertEqual(Solution().addBinary("11", "1"), "100")

    def test_addBinary2(self):
        self.assertEqual(Solution().addBinary("1010", "1011"), "10101")
