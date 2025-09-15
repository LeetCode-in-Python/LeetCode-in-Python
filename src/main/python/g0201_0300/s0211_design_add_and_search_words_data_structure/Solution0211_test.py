import unittest
from Solution0211 import WordDictionary

class SolutionTest(unittest.TestCase):
    def test_worldDataStructure(self):
        input_words = ["bad", "dad", "mad"]
        dictionary = WordDictionary()
        for s in input_words:
            dictionary.addWord(s)
        self.assertFalse(dictionary.search("pad"))
        self.assertTrue(dictionary.search("bad"))
        self.assertTrue(dictionary.search(".ad"))
        self.assertTrue(dictionary.search("b.."))
