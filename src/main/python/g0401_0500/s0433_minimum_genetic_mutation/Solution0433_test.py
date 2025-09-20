import unittest
from Solution0433 import Solution

class SolutionTest(unittest.TestCase):
    def test_minMutation(self):
        self.assertEqual(
            Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]),
            1
        )

    def test_minMutation2(self):
        self.assertEqual(
            Solution().minMutation(
                "AACCGGTT", 
                "AAACGGTA", 
                ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
            ),
            2
        )

    def test_minMutation3(self):
        self.assertEqual(
            Solution().minMutation(
                "AAAAACCC",
                "AACCCCCC",
                ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
            ),
            3
        )
