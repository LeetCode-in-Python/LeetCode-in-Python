import unittest
from Solution0215 import Solution

class SolutionTest(unittest.TestCase):
    def test_findKthLargest(self):
        self.assertEqual(Solution().findKthLargest([3,2,1,5,6,4], 2), 5)

    def test_findKthLargest2(self):
        self.assertEqual(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)
