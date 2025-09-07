import unittest
from Solution0131 import Solution

def sort_nested(lists):
    return sorted(lists)

class SolutionTest(unittest.TestCase):
    def test_partition(self):
        res = Solution().partition("aab")
        expected = [["a","a","b"],["aa","b"]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_partition2(self):
        res = Solution().partition("a")
        expected = [["a"]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_partition3(self):
        res = Solution().partition("racecar")
        expected = [["r","a","c","e","c","a","r"],["r","a","cec","a","r"],["r","aceca","r"],["racecar"]]
        self.assertEqual(sort_nested(res), sort_nested(expected))
