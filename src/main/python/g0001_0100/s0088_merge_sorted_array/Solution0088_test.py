import unittest
from Solution0088 import Solution

class SolutionTest(unittest.TestCase):
    def test_merge(self):
        array = [1, 2, 3, 0, 0, 0]
        Solution().merge(array, 3, [2, 5, 6], 3)
        self.assertEqual(array, [1, 2, 2, 3, 5, 6])

    def test_merge2(self):
        array = [1]
        Solution().merge(array, 1, [], 0)
        self.assertEqual(array, [1])
