import unittest
from Solution0009 import Solution

class SolutionTest(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(Solution().isPalindrome(121), True)

    def test_isPalindrome2(self):
        self.assertEqual(Solution().isPalindrome(-121), False)

    def test_isPalindrome3(self):
        self.assertEqual(Solution().isPalindrome(10), False)
