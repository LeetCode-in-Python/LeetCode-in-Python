import unittest
from Solution0373 import Solution

class SolutionTest(unittest.TestCase):
    def test_kSmallestPairs(self):
        self.assertEqual(
            Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3),
            [[1, 2], [1, 4], [1, 6]]
        )

    def test_kSmallestPairs2(self):
        self.assertEqual(
            Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 2),
            [[1, 1], [1, 1]]
        )

    def test_kSmallestPairs3(self):
        self.assertEqual(
            Solution().kSmallestPairs([1, 2], [3], 3),
            [[1, 3], [2, 3]]
        )
