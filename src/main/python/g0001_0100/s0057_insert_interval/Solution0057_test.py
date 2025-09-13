import unittest
from Solution0057 import Solution

class SolutionTest(unittest.TestCase):
    def test_insert(self):
        self.assertEqual(
            Solution().insert([[1, 3], [6, 9]], [2, 5]),
            [[1, 5], [6, 9]]
        )

    def test_insert2(self):
        self.assertEqual(
            Solution().insert(
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
            ),
            [[1, 2], [3, 10], [12, 16]]
        )
