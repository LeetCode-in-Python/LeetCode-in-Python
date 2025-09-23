import unittest
from Solution0763 import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partitionLabels(self):
        self.assertEqual(
            self.solution.partitionLabels("ababcbacadefegdehijhklij"),
            [9, 7, 8]
        )

    def test_partitionLabels2(self):
        self.assertEqual(
            self.solution.partitionLabels("eccbbbbdec"),
            [10]
        )
