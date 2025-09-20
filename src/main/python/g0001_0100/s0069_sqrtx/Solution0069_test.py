import unittest
from Solution0069 import Solution

class SolutionTest(unittest.TestCase):
    def test_mySqrt(self):
        self.assertEqual(Solution().mySqrt(4), 2)

    def test_mySqrt2(self):
        self.assertEqual(Solution().mySqrt(8), 2)
