import unittest
from Solution0347 import Solution

class SolutionTest(unittest.TestCase):
    def test_topKFrequent(self):
        self.assertEqual(
            Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2),
            [1, 2]
        )

    def test_topKFrequent2(self):
        self.assertEqual(
            Solution().topKFrequent([1], 1),
            [1]
        )
