import unittest
from Solution0242 import Solution

class SolutionTest(unittest.TestCase):
    def test_isAnagram(self):
        self.assertTrue(Solution().isAnagram("anagram", "nagaram"))

    def test_isAnagram2(self):
        self.assertFalse(Solution().isAnagram("rat", "car"))
