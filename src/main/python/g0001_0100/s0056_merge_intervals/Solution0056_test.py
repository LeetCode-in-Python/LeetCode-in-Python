import unittest
from Solution0056 import Solution

class SolutionTest(unittest.TestCase):
    def test_merge(self):
        res = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(res, expected)

    def test_merge2(self):
        res = Solution().merge([[1,4],[4,5]])
        expected = [[1,5]]
        self.assertEqual(res, expected)

    def test_merge3(self):
        res = Solution().merge([[1,4],[0,4]])
        expected = [[0,4]]
        self.assertEqual(res, expected)
