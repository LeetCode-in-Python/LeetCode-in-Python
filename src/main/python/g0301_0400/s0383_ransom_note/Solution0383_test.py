import unittest
from Solution0383 import Solution

class SolutionTest(unittest.TestCase):
    def test_canConstruct(self):
        self.assertFalse(Solution().canConstruct("a", "b"))

    def test_canConstruct2(self):
        self.assertFalse(Solution().canConstruct("aa", "ab"))

    def test_canConstruct3(self):
        self.assertTrue(Solution().canConstruct("aa", "aab"))
