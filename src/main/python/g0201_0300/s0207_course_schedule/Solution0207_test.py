import unittest
from Solution0207 import Solution

class SolutionTest(unittest.TestCase):
    def test_canFinish(self):
        self.assertTrue(Solution().canFinish(2, [[1,0]]))

    def test_canFinish2(self):
        self.assertFalse(Solution().canFinish(2, [[1,0],[0,1]]))

    def test_canFinish3(self):
        self.assertTrue(Solution().canFinish(1, []))
