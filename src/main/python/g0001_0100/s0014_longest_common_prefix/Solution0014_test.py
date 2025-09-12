import unittest
from Solution0014 import Solution

class SolutionTest(unittest.TestCase):
    def test_longestCommonPrefix(self):
        self.assertEqual(Solution().longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_longestCommonPrefix2(self):
        self.assertEqual(Solution().longestCommonPrefix(["dog", "racecar", "car"]), "")
