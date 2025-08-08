import unittest
from Solution0007 import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_reverse(self):
        self.assertEqual(Solution().reverse(123), 321)

    def test_reverse2(self):
        self.assertEqual(Solution().reverse(-123), -321)

    def test_reverse3(self):
        self.assertEqual(Solution().reverse(120), 21)
