import unittest
from Solution0104 import Solution, TreeNode

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
    def test_maxDepth(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(Solution().maxDepth(root), 3)

    def test_maxDepth2(self):
        root = build_tree([1, None, 2])
        self.assertEqual(Solution().maxDepth(root), 2)

    def test_maxDepth3(self):
        root = build_tree([])
        self.assertEqual(Solution().maxDepth(root), 0)
