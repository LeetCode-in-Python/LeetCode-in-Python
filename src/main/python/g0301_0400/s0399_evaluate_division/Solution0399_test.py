import unittest
from Solution0399 import Solution

class SolutionTest(unittest.TestCase):
    def test_calcEquation(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        result = Solution().calcEquation(equations, values, queries)
        for i in range(len(expected)):
            self.assertAlmostEqual(result[i], expected[i], places=5)

    def test_calcEquation2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75000, 0.40000, 5.00000, 0.20000]
        result = Solution().calcEquation(equations, values, queries)
        for i in range(len(expected)):
            self.assertAlmostEqual(result[i], expected[i], places=5)

    def test_calcEquation3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.50000, 2.00000, -1.00000, -1.00000]
        result = Solution().calcEquation(equations, values, queries)
        for i in range(len(expected)):
            self.assertAlmostEqual(result[i], expected[i], places=5)
