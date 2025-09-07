import unittest
from Solution0101 import Solution, TreeNode

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
    def test_isSymmetric(self):
        root = build_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(Solution().isSymmetric(root))

    def test_isSymmetric2(self):
        root = build_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(Solution().isSymmetric(root))

    def test_isSymmetric3(self):
        root = build_tree([1])
        self.assertTrue(Solution().isSymmetric(root))
