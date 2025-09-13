import unittest
from Solution0066 import Solution

class SolutionTest(unittest.TestCase):
    def test_plusOne(self):
        self.assertEqual(Solution().plusOne([1, 2, 3]), [1, 2, 4])

    def test_plusOne2(self):
        self.assertEqual(Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_plusOne3(self):
        self.assertEqual(Solution().plusOne([0]), [1])

    def test_plusOne4(self):
        self.assertEqual(Solution().plusOne([9]), [1, 0])
