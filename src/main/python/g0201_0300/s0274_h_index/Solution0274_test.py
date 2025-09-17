import unittest
from Solution0274 import Solution

class SolutionTest(unittest.TestCase):
    def test_hIndex(self):
        self.assertEqual(Solution().hIndex([3, 0, 6, 1, 5]), 3)

    def test_hIndex2(self):
        self.assertEqual(Solution().hIndex([1, 3, 1]), 1)
