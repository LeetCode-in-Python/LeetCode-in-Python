import unittest
from Solution0135 import Solution

class SolutionTest(unittest.TestCase):
    def test_candy(self):
        self.assertEqual(Solution().candy([1, 0, 2]), 5)

    def test_candy2(self):
        self.assertEqual(Solution().candy([1, 2, 2]), 4)
