import unittest
from Solution0134 import Solution

class SolutionTest(unittest.TestCase):
    def test_canCompleteCircuit(self):
        self.assertEqual(
            Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
            3
        )

    def test_canCompleteCircuit2(self):
        self.assertEqual(
            Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]),
            -1
        )
