import unittest
from Solution0125 import Solution

class SolutionTest(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(Solution().isPalindrome("A man, a plan, a canal: Panama"))

    def test_isPalindrome2(self):
        self.assertFalse(Solution().isPalindrome("race a car"))

    def test_isPalindrome3(self):
        self.assertTrue(Solution().isPalindrome(" "))
