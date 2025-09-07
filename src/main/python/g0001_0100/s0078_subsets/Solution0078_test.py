import unittest
from Solution0078 import Solution

def sort_nested(lists):
    return sorted([sorted(x) for x in lists])

class SolutionTest(unittest.TestCase):
    def test_subsets(self):
        res = Solution().subsets([1,2,3])
        expected = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_subsets2(self):
        res = Solution().subsets([0])
        expected = [[],[0]]
        self.assertEqual(sort_nested(res), sort_nested(expected))
