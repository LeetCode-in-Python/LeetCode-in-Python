import unittest
from Solution0046 import Solution

def sort_nested(lists):
    return sorted([sorted(x) for x in lists])

class SolutionTest(unittest.TestCase):
    def test_permute(self):
        res = Solution().permute([1,2,3])
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_permute2(self):
        res = Solution().permute([0,1])
        expected = [[0,1],[1,0]]
        self.assertEqual(sort_nested(res), sort_nested(expected))

    def test_permute3(self):
        res = Solution().permute([1])
        expected = [[1]]
        self.assertEqual(sort_nested(res), sort_nested(expected))
