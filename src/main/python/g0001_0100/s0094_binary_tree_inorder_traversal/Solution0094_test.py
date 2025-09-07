import unittest
from Solution0094 import Solution, TreeNode

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class SolutionTest(unittest.TestCase):
    def test_inorderTraversal(self):
        root = build_tree([1, None, 2, 3])
        self.assertEqual(Solution().inorderTraversal(root), [1, 3, 2])

    def test_inorderTraversal2(self):
        root = build_tree([])
        self.assertEqual(Solution().inorderTraversal(root), [])

    def test_inorderTraversal3(self):
        root = build_tree([1])
        self.assertEqual(Solution().inorderTraversal(root), [1])
