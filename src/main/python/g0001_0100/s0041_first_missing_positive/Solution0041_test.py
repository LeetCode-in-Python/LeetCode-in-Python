import unittest
from Solution0041 import Solution

class SolutionTest(unittest.TestCase):
    def test_firstMissingPositive(self):
        self.assertEqual(Solution().firstMissingPositive([1,2,0]), 3)

    def test_firstMissingPositive2(self):
        self.assertEqual(Solution().firstMissingPositive([3,4,-1,1]), 2)

    def test_firstMissingPositive3(self):
        self.assertEqual(Solution().firstMissingPositive([7,8,9,11,12]), 1)
