import unittest
from Solution0050 import Solution

class SolutionTest(unittest.TestCase):
    def test_myPow(self):
        self.assertEqual(Solution().myPow(2.00000, 10), 1024.00000)

    def test_myPow2(self):
        self.assertEqual(Solution().myPow(2.10000, 3), 9.261000000000001)

    def test_myPow3(self):
        self.assertEqual(Solution().myPow(2.00000, -2), 0.25000)
