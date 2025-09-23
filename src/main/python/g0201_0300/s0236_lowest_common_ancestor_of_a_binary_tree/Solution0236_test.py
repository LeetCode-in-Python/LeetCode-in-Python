import unittest
from Solution0236 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_lowestCommonAncestor(self):
        leftNodeLeftNode = TreeNode(6)
        leftNodeRightNode = TreeNode(2, TreeNode(7), TreeNode(4))
        leftNode = TreeNode(5, leftNodeLeftNode, leftNodeRightNode)
        rightNode = TreeNode(1, TreeNode(0), TreeNode(8))
        root = TreeNode(3, leftNode, rightNode)
        self.assertEqual(
            Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(1)).val,
            3
        )

    def test_lowestCommonAncestor2(self):
        leftNodeLeftNode = TreeNode(6)
        leftNodeRightNode = TreeNode(2, TreeNode(7), TreeNode(4))
        leftNode = TreeNode(5, leftNodeLeftNode, leftNodeRightNode)
        rightNode = TreeNode(1, TreeNode(0), TreeNode(8))
        root = TreeNode(3, leftNode, rightNode)
        self.assertEqual(
            Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(4)).val,
            5
        )

    def test_lowestCommonAncestor3(self):
        root = TreeNode(2, TreeNode(1), None)
        self.assertEqual(
            Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(1)).val,
            2
        )
