import unittest
import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_two_sum(self):
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum2(self):
        self.assertEqual(self.sol.twoSum([3, 2, 4], 6), [1, 2])

    def test_two_sum3(self):
        self.assertEqual(self.sol.twoSum([3, 3], 6), [0, 1])

    def test_two_sum4(self):
        self.assertEqual(self.sol.twoSum([3, 3], 7), [-1, -1])
