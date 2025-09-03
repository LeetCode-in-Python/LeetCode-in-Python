import unittest
from Solution0031 import Solution

class SolutionTest(unittest.TestCase):
    def test_nextPermutation(self):
        array = [1, 2, 3]
        Solution().nextPermutation(array)
        self.assertEqual(array, [1, 3, 2])

    def test_nextPermutation2(self):
        array = [3, 2, 1]
        Solution().nextPermutation(array)
        self.assertEqual(array, [1, 2, 3])

    def test_nextPermutation3(self):
        array = [1, 1, 5]
        Solution().nextPermutation(array)
        self.assertEqual(array, [1, 5, 1]) 
