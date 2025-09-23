import unittest
from Solution0283 import Solution

class SolutionTest(unittest.TestCase):
    def test_moveZeroes(self):
        array = [0, 1, 0, 3, 12]
        Solution().moveZeroes(array)
        self.assertEqual(array, [1, 3, 12, 0, 0])

    def test_moveZeroes2(self):
        array = [0]
        Solution().moveZeroes(array)
        self.assertEqual(array, [0])
