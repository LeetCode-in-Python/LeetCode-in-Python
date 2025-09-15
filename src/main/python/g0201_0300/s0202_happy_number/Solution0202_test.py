import unittest
from Solution0202 import Solution

class SolutionTest(unittest.TestCase):
    def test_isHappy(self):
        self.assertTrue(Solution().isHappy(19))

    def test_isHappy2(self):
        self.assertFalse(Solution().isHappy(2))

