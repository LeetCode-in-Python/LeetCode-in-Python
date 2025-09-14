import unittest
from Solution0112 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_hasPathSum(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        self.assertTrue(Solution().hasPathSum(root, 22))

    def test_hasPathSum2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(Solution().hasPathSum(root, 22))

    def test_hasPathSum3(self):
        self.assertFalse(Solution().hasPathSum(None, 0))
