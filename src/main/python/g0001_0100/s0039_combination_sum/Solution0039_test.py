import unittest
from Solution0039 import Solution

def sort_nested(lists):
    return sorted([sorted(x) for x in lists])

class SolutionTest(unittest.TestCase):
    def test_combinationSum(self):
        res = Solution().combinationSum([2,3,6,7], 7)
        self.assertEqual(sort_nested(res), sort_nested([[7],[2,2,3]]))

    def test_combinationSum2(self):
        res = Solution().combinationSum([2,3,5], 8)
        self.assertEqual(sort_nested(res), sort_nested([[2,2,2,2],[2,3,3],[3,5]]))

    def test_combinationSum3(self):
        res = Solution().combinationSum([2], 1)
        self.assertEqual(sort_nested(res), sort_nested([]))
