import unittest
from Solution0009 import Solution

class SolutionTest(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(Solution().isPalindrome(121))

    def test_isPalindrome2(self):
        self.assertFalse(Solution().isPalindrome(-121))

    def test_isPalindrome3(self):
        self.assertFalse(Solution().isPalindrome(10))
