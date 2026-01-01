import unittest
from Solution0236 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_lowestCommonAncestor(self):
        left_node_left_node = TreeNode(6)
        left_node_right_node = TreeNode(2, TreeNode(7), TreeNode(4))
        left_node = TreeNode(5, left_node_left_node, left_node_right_node)
        right_node = TreeNode(1, TreeNode(0), TreeNode(8))
        root = TreeNode(3, left_node, right_node)
        self.assertEqual(
            Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(1)).val,
            3
        )

    def test_lowestCommonAncestor2(self):
        left_node_left_node = TreeNode(6)
        left_node_right_node = TreeNode(2, TreeNode(7), TreeNode(4))
        left_node = TreeNode(5, left_node_left_node, left_node_right_node)
        right_node = TreeNode(1, TreeNode(0), TreeNode(8))
        root = TreeNode(3, left_node, right_node)
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
