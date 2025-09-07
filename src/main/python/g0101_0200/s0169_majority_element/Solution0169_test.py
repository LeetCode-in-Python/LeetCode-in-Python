import unittest
from Solution0169 import Solution

class SolutionTest(unittest.TestCase):
    def test_majorityElement(self):
        self.assertEqual(Solution().majorityElement([3,2,3]), 3)

    def test_majorityElement2(self):
        self.assertEqual(Solution().majorityElement([2,2,1,1,1,2,2]), 2)

    def test_majorityElement3(self):
        self.assertEqual(Solution().majorityElement([1]), 1)

    def test_majorityElement4(self):
        self.assertEqual(Solution().majorityElement([1,1,1,2,2,2,2]), 2)
