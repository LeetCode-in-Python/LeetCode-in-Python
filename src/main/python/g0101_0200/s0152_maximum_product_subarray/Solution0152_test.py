import unittest
from Solution0152 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxProduct(self):
        self.assertEqual(Solution().maxProduct([2,3,-2,4]), 6)

    def test_maxProduct2(self):
        self.assertEqual(Solution().maxProduct([-2,0,-1]), 0)

    def test_maxProduct3(self):
        self.assertEqual(Solution().maxProduct([-2]), -2)

    def test_maxProduct4(self):
        self.assertEqual(Solution().maxProduct([-2,3,-4]), 24)
