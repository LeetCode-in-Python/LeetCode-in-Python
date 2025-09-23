import unittest
from Solution0239 import Solution

class SolutionTest(unittest.TestCase):
    def test_maxSlidingWindow(self):
        self.assertEqual(
            Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7]
        )

    def test_maxSlidingWindow2(self):
        self.assertEqual(
            Solution().maxSlidingWindow([1], 1),
            [1]
        )
