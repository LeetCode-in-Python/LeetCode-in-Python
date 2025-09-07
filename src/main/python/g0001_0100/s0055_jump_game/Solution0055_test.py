import unittest
from Solution0055 import Solution

class SolutionTest(unittest.TestCase):
    def test_canJump(self):
        self.assertTrue(Solution().canJump([2,3,1,1,4]))

    def test_canJump2(self):
        self.assertFalse(Solution().canJump([3,2,1,0,4]))

    def test_canJump3(self):
        self.assertTrue(Solution().canJump([1]))
