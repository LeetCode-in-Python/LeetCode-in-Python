import unittest
from Solution0049 import Solution

def sort_nested(lists):
    return sorted([sorted(x) for x in lists])

class SolutionTest(unittest.TestCase):
    def test_groupAnagrams(self):
        res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_groupAnagrams2(self):
        res = Solution().groupAnagrams([""])
        expected = [[""]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_groupAnagrams3(self):
        res = Solution().groupAnagrams(["a"])
        expected = [["a"]]
        self.assertEqual(sort_nested(res), sort_nested(expected))
