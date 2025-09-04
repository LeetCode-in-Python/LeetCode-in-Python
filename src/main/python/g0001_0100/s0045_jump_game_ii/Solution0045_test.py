import unittest
from Solution0045 import Solution

class SolutionTest(unittest.TestCase):
    def test_jump(self):
        self.assertEqual(Solution().jump([2,3,1,1,4]), 2)

    def test_jump2(self):
        self.assertEqual(Solution().jump([2,3,0,1,4]), 2)
