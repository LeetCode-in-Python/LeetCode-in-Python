import unittest
from Solution0129 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_sumNumbers(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(Solution().sumNumbers(root), 25)

    def test_sumNumbers2(self):
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        self.assertEqual(Solution().sumNumbers(root), 1026)
