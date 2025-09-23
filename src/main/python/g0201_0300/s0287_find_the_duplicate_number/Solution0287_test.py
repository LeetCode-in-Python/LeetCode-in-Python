import unittest
from Solution0287 import Solution

class SolutionTest(unittest.TestCase):
    def test_findDuplicate(self):
        self.assertEqual(Solution().findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_findDuplicate2(self):
        self.assertEqual(Solution().findDuplicate([3, 1, 3, 4, 2]), 3)

    def test_findDuplicate3(self):
        self.assertEqual(Solution().findDuplicate([1, 1]), 1)

    def test_findDuplicate4(self):
        self.assertEqual(Solution().findDuplicate([1, 1, 2]), 1)
