import unittest
from Solution0205 import Solution

class SolutionTest(unittest.TestCase):
    def test_isIsomorphic(self):
        self.assertTrue(Solution().isIsomorphic("egg", "add"))

    def test_isIsomorphic2(self):
        self.assertFalse(Solution().isIsomorphic("foo", "bar"))

    def test_isIsomorphic3(self):
        self.assertTrue(Solution().isIsomorphic("paper", "title"))

