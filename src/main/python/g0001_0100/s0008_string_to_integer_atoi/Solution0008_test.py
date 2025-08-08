import unittest
from Solution0008 import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_myAtoi(self):
        self.assertEqual(Solution().myAtoi("42"), 42)

    def test_myAtoi2(self):
        self.assertEqual(Solution().myAtoi("   -42"), -42)

    def test_myAtoi3(self):
        self.assertEqual(Solution().myAtoi("4193 with words"), 4193)

    def test_myAtoi4(self):
        self.assertEqual(Solution().myAtoi("words and 987"), 0)

    def test_myAtoi5(self):
        self.assertEqual(Solution().myAtoi("-91283472332"), -2147483648)
