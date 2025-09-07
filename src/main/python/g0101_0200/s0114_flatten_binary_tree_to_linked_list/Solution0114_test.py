import unittest
from Solution0114 import Solution, TreeNode

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

def flatten_to_list(root):
    result = []
    current = root
    while current:
        result.append(current.val)
        current = current.right
    return result


class SolutionTest(unittest.TestCase):
    def test_flatten(self):
        root = build_tree([1, 2, 5, 3, 4, None, 6])
        Solution().flatten(root)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten_to_list(root), expected)

    def test_flatten2(self):
        root = build_tree([])
        Solution().flatten(root)
        self.assertIsNone(root)

    def test_flatten3(self):
        root = build_tree([0])
        Solution().flatten(root)
        expected = [0]
        self.assertEqual(flatten_to_list(root), expected)
