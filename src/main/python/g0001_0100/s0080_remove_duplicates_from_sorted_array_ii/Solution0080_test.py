import unittest
from Solution0080 import Solution

class SolutionTest(unittest.TestCase):
    def test_removeDuplicates(self):
        array = [1, 1, 1, 2, 2, 3]
        end = Solution().removeDuplicates(array)
        self.assertEqual(array[:end], [1, 1, 2, 2, 3])

    def test_removeDuplicates2(self):
        array = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        end = Solution().removeDuplicates(array)
        self.assertEqual(array[:end], [0, 0, 1, 1, 2, 3, 3])
