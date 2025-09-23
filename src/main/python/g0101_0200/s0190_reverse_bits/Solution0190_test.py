import unittest
from Solution0190 import Solution

class SolutionTest(unittest.TestCase):
    def test_reverseBits(self):
        self.assertEqual(
            Solution().reverseBits(0b00000010100101000001111010011100),
            0b00111001011110000010100101000000
        )

    def test_reverseBits2(self):
        self.assertEqual(
            Solution().reverseBits(0b11111111111111111111111111111101),
            0b10111111111111111111111111111111
        )
