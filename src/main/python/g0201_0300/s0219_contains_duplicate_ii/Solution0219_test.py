import unittest
from Solution0219 import Solution

class SolutionTest(unittest.TestCase):
    def test_containsNearbyDuplicate(self):
        self.assertTrue(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_containsNearbyDuplicate2(self):
        self.assertTrue(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_containsNearbyDuplicate3(self):
        self.assertFalse(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
