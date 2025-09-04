import unittest
from Solution0033 import Solution

class SolutionTest(unittest.TestCase):
    def test_search(self):
        self.assertEqual(Solution().search([4,5,6,7,0,1,2], 0), 4)

    def test_search2(self):
        self.assertEqual(Solution().search([4,5,6,7,0,1,2], 3), -1)

    def test_search3(self):
        self.assertEqual(Solution().search([1], 0), -1)
