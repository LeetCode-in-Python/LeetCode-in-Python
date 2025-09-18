import unittest
from Solution0222 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_countNodes(self):
        left_left = TreeNode(4)
        left_right = TreeNode(5)
        left = TreeNode(2, left_left, left_right)
        right_left = TreeNode(6)
        right = TreeNode(3, right_left, None)
        root = TreeNode(1, left, right)
        self.assertEqual(Solution().countNodes(root), 6)

    def test_countNodes_null(self):
        self.assertEqual(Solution().countNodes(None), 0)

    def test_countNodes_single(self):
        self.assertEqual(Solution().countNodes(TreeNode(1)), 1)
