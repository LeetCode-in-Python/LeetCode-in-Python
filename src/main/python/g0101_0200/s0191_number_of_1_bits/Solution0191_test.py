import unittest
from Solution0191 import Solution

class SolutionTest(unittest.TestCase):
    def test_hammingWeight(self):
        self.assertEqual(Solution().hammingWeight(0b00000000000000000000000000001011), 3)

    def test_hammingWeight2(self):
        self.assertEqual(Solution().hammingWeight(0b00000000000000000000000010000000), 1)
