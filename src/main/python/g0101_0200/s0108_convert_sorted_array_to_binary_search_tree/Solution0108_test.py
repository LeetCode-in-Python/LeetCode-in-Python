import unittest
from Solution0108 import Solution

class SolutionTest(unittest.TestCase):
    def test_sortedArrayToBST(self):
        actual = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
        result = self._tree_to_string(actual)
        self.assertEqual(result, "0,-10,null,-3,null,null,5,null,9,null,null")

    def test_sortedArrayToBST2(self):
        actual = Solution().sortedArrayToBST([1, 3])
        result = self._tree_to_string(actual)
        self.assertEqual(result, "1,null,3,null,null")

    def _tree_to_string(self, root):
        if root is None:
            return ""
        result = []
        self._preorder_traversal(root, result)
        return ",".join(map(str, result))

    def _preorder_traversal(self, node, result):
        if node is None:
            result.append("null")
            return
        result.append(node.val)
        self._preorder_traversal(node.left, result)
        self._preorder_traversal(node.right, result)
