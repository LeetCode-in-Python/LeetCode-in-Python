import unittest
from Solution0530 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_getMinimumDifference(self):
        # Tree: [4, 2, 6, 1, 3]
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(Solution().getMinimumDifference(root), 1)

    def test_getMinimumDifference2(self):
        # Tree: [1, 0, 48, null, null, 12, 49]
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(48)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(49)
        self.assertEqual(Solution().getMinimumDifference(root), 1)
