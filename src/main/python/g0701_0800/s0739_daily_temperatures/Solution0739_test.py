import unittest
from Solution0739 import Solution

import unittest

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_dailyTemperatures(self):
        self.assertEqual(
            self.solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0]
        )

    def test_dailyTemperatures2(self):
        self.assertEqual(
            self.solution.dailyTemperatures([30, 40, 50, 60]),
            [1, 1, 1, 0]
        )

    def test_dailyTemperatures3(self):
        self.assertEqual(
            self.solution.dailyTemperatures([30, 60, 90]),
            [1, 1, 0]
        )
