import unittest
from Solution0106 import Solution

class SolutionTest(unittest.TestCase):
    def test_buildTree(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        actual = Solution().buildTree(inorder, postorder)
        # Convert tree to string representation for comparison
        result = self._tree_to_string(actual)
        self.assertEqual(result, "9,3,15,20,7")

    def test_buildTree2(self):
        inorder = [-1]
        postorder = [-1]
        actual = Solution().buildTree(inorder, postorder)
        result = self._tree_to_string(actual)
        self.assertEqual(result, "-1")

    def _tree_to_string(self, root):
        if root is None:
            return ""
        result = []
        self._inorder_traversal(root, result)
        return ",".join(map(str, result))

    def _inorder_traversal(self, node, result):
        if node is None:
            return
        self._inorder_traversal(node.left, result)
        result.append(node.val)
        self._inorder_traversal(node.right, result)
