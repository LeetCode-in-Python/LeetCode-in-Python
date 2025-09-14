import unittest
from Solution0127 import Solution

class SolutionTest(unittest.TestCase):
    def test_ladderLength(self):
        self.assertEqual(
            Solution().ladderLength(
                "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
            ),
            5
        )

    def test_ladderLength2(self):
        self.assertEqual(
            Solution().ladderLength(
                "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
            ),
            0
        )
