import unittest
from Solution0030 import Solution

class SolutionTest(unittest.TestCase):
    def test_findSubstring(self):
        self.assertEqual(
            Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]),
            [0, 9]
        )

    def test_findSubstring2(self):
        self.assertEqual(
            Solution().findSubstring(
                "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
            ),
            []
        )

    def test_findSubstring3(self):
        self.assertEqual(
            Solution().findSubstring(
                "barfoofoobarthefoobarman", ["bar", "foo", "the"]
            ),
            [6, 9, 12]
        )
