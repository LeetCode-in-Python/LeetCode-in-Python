import unittest
from Solution0228 import Solution

class SolutionTest(unittest.TestCase):
    def test_summaryRanges(self):
        self.assertEqual(
            Solution().summaryRanges([0, 1, 2, 4, 5, 7]),
            ["0->2", "4->5", "7"],
        )

    def test_summaryRanges2(self):
        self.assertEqual(
            Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]),
            ["0", "2->4", "6", "8->9"],
        )
