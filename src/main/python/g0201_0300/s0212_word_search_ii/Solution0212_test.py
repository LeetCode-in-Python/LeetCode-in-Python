import unittest
from Solution0212 import Solution

class SolutionTest(unittest.TestCase):
    def test_findWords(self):
        board = [
            ['o', 'a', 'a', 'n'], 
            ['e', 't', 'a', 'e'], 
            ['i', 'h', 'k', 'r'], 
            ['i', 'f', 'l', 'v']
        ]
        words = ["oath", "pea", "eat", "rain"]
        expected = ["oath", "eat"]
        result = Solution().findWords(board, words)
        self.assertEqual(sorted(result), sorted(expected))

    def test_findWords2(self):
        board = [['a', 'b'], ['c', 'd']]
        words = ["abcb"]
        self.assertEqual(Solution().findWords(board, words), [])
