import unittest
from Solution0128 import Solution

class SolutionTest(unittest.TestCase):
    def test_longestConsecutive(self):
        self.assertEqual(Solution().longestConsecutive([100,4,200,1,3,2]), 4)

    def test_longestConsecutive2(self):
        self.assertEqual(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)

    def test_longestConsecutive3(self):
        self.assertEqual(Solution().longestConsecutive([]), 0)
