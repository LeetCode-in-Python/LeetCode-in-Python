import unittest
from Solution0017 import Solution

class SolutionTest(unittest.TestCase):
    def test_letterCombinations(self):
        self.assertEqual(
            Solution().letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )

    def test_letterCombinations2(self):
        self.assertEqual(Solution().letterCombinations(""), [])

    def test_letterCombinations3(self):
        self.assertEqual(Solution().letterCombinations("2"), ["a", "b", "c"])

    def test_letterCombinations4(self):
        self.assertEqual(Solution().letterCombinations("4"), ["g", "h", "i"])

    def test_letterCombinations5(self):
        self.assertEqual(Solution().letterCombinations("5"), ["j", "k", "l"])

    def test_letterCombinations6(self):
        self.assertEqual(Solution().letterCombinations("6"), ["m", "n", "o"])

    def test_letterCombinations7(self):
        self.assertEqual(Solution().letterCombinations("7"), ["p", "q", "r", "s"])

    def test_letterCombinations8(self):
        self.assertEqual(Solution().letterCombinations("8"), ["t", "u", "v"])

    def test_letterCombinations9(self):
        self.assertEqual(Solution().letterCombinations("9"), ["w", "x", "y", "z"])
