import unittest
from Solution0238 import Solution

class SolutionTest(unittest.TestCase):
    def test_productExceptSelf(self):
        self.assertEqual(
            Solution().productExceptSelf([1, 2, 3, 4]),
            [24, 12, 8, 6]
        )

    def test_productExceptSelf2(self):
        self.assertEqual(
            Solution().productExceptSelf([-1, 1, 0, -3, 3]),
            [0, 0, 9, 0, 0]
        )
