import unittest
from Solution0042 import Solution

class SolutionTest(unittest.TestCase):
    def test_trap(self):
        self.assertEqual(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

    def test_trap2(self):
        self.assertEqual(Solution().trap([4,2,0,3,2,5]), 9)
