import unittest
from Solution0103 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_zigzagLevelOrder(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        actual = Solution().zigzagLevelOrder(root)
        expected = [[3], [20, 9], [15, 7]]
        self.assertEqual(actual, expected)

    def test_zigzagLevelOrder2(self):
        root = TreeNode(1)
        actual = Solution().zigzagLevelOrder(root)
        expected = [[1]]
        self.assertEqual(actual, expected)

    def test_zigzagLevelOrder3(self):
        actual = Solution().zigzagLevelOrder(None)
        expected = []
        self.assertEqual(actual, expected)
