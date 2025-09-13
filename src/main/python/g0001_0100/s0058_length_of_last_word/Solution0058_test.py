import unittest
from Solution0058 import Solution

class SolutionTest(unittest.TestCase):
    def test_lengthOfLastWord(self):
        self.assertEqual(Solution().lengthOfLastWord("Hello World"), 5)

    def test_lengthOfLastWord2(self):
        self.assertEqual(Solution().lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_lengthOfLastWord3(self):
        self.assertEqual(Solution().lengthOfLastWord("luffy is still joyboy"), 6)
