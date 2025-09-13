import unittest
from Solution0054 import Solution

class SolutionTest(unittest.TestCase):
    def test_spiralOrder(self):
        self.assertEqual(
            Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        )

    def test_spiralOrder2(self):
        self.assertEqual(
            Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        )
