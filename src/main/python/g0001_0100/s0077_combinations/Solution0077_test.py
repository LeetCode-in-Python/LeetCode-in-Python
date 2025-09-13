import unittest
from Solution0077 import Solution


class SolutionTest(unittest.TestCase):
    def test_combine(self):
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        actual = Solution().combine(4, 2)
        # Sort both lists for comparison since order might differ
        expected.sort()
        actual.sort()
        self.assertEqual(actual, expected)

    def test_combine2(self):
        expected = [[1]]
        actual = Solution().combine(1, 1)
        self.assertEqual(actual, expected)
