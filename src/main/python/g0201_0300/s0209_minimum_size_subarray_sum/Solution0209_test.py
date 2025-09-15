import unittest
from Solution0209 import Solution

class SolutionTest(unittest.TestCase):
    def test_minSubArrayLen(self):
        self.assertEqual(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_minSubArrayLen2(self):
        self.assertEqual(Solution().minSubArrayLen(4, [1, 4, 4]), 1)

    def test_minSubArrayLen3(self):
        self.assertEqual(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)

