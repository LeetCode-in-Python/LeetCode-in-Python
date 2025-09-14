import unittest
from Solution0199 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_rightSideView(self):
        left = TreeNode(2)
        left.right = TreeNode(5)
        right = TreeNode(3)
        right.right = TreeNode(4)
        root = TreeNode(1, left, right)
        self.assertEqual(Solution().rightSideView(root), [1, 3, 4])

    def test_rightSideView2(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(Solution().rightSideView(root), [1, 3])

