import unittest
from Solution0198 import Solution

class SolutionTest(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(Solution().rob([1,2,3,1]), 4)

    def test_rob2(self):
        self.assertEqual(Solution().rob([2,7,9,3,1]), 12)

    def test_rob3(self):
        self.assertEqual(Solution().rob([]), 0)
