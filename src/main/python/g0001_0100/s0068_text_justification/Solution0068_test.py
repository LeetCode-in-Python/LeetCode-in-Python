import unittest
from Solution0068 import Solution

class SolutionTest(unittest.TestCase):
    def test_fullJustify(self):
        input_words = ["This", "is", "an", "example", "of", "text", "justification."]
        actual = Solution().fullJustify(input_words, 16)
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        self.assertEqual(actual, expected)

    def test_fullJustify2(self):
        input_words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        actual = Solution().fullJustify(input_words, 16)
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        self.assertEqual(actual, expected)

    def test_fullJustify3(self):
        input_words = [
            "Science", "is", "what", "we", "understand", "well", "enough", "to",
            "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"
        ]
        actual = Solution().fullJustify(input_words, 20)
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        self.assertEqual(actual, expected)
