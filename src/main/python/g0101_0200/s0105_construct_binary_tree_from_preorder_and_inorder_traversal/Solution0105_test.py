import unittest
from Solution0105 import Solution, TreeNode

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

class SolutionTest(unittest.TestCase):
    def test_buildTree(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        result = Solution().buildTree(preorder, inorder)
        # Check that the tree structure is correct by comparing values
        self.assertEqual(result.val, 3)
        self.assertEqual(result.left.val, 9)
        self.assertEqual(result.right.val, 20)

    def test_buildTree2(self):
        preorder = [-1]
        inorder = [-1]
        result = Solution().buildTree(preorder, inorder)
        self.assertEqual(result.val, -1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)
