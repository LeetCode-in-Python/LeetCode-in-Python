import unittest
from Solution0394 import Solution

class SolutionTest(unittest.TestCase):
    def test_decodeString(self):
        self.assertEqual(Solution().decodeString("3[a]2[bc]"), "aaabcbc")

    def test_decodeString2(self):
        self.assertEqual(Solution().decodeString("3[a2[c]]"), "accaccacc")

    def test_decodeString3(self):
        self.assertEqual(Solution().decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_decodeString4(self):
        self.assertEqual(Solution().decodeString("abc3[cd]xyz"), "abccdcdcdxyz")
