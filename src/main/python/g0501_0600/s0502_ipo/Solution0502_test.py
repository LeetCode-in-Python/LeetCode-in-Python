import unittest
from Solution0502 import Solution

class SolutionTest(unittest.TestCase):
    def test_findMaximizedCapital(self):
        self.assertEqual(
            Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]),
            4
        )

    def test_findMaximizedCapital2(self):
        self.assertEqual(
            Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]),
            6
        )
