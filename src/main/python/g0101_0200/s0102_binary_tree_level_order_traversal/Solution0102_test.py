import unittest
from Solution0102 import Solution, TreeNode

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
    def test_levelOrder(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        expected = [[3], [9, 20], [15, 7]]
        self.assertEqual(Solution().levelOrder(root), expected)

    def test_levelOrder2(self):
        root = build_tree([1])
        expected = [[1]]
        self.assertEqual(Solution().levelOrder(root), expected)

    def test_levelOrder3(self):
        root = build_tree([])
        expected = []
        self.assertEqual(Solution().levelOrder(root), expected)
