import unittest
from Solution0100 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_isSameTree(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        self.assertTrue(Solution().isSameTree(p, q))

    def test_isSameTree2(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        q = TreeNode(1)
        q.right = TreeNode(2)
        self.assertFalse(Solution().isSameTree(p, q))

    def test_isSameTree3(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        self.assertFalse(Solution().isSameTree(p, q))

    def test_isSameTree4(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        self.assertFalse(Solution().isSameTree(p, None))

    def test_isSameTree5(self):
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        self.assertFalse(Solution().isSameTree(None, q))

    def test_isSameTree6(self):
        self.assertTrue(Solution().isSameTree(None, None))
