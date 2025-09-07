import unittest
from Solution0098 import Solution, TreeNode

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
    def test_isValidBST(self):
        root = build_tree([2, 1, 3])
        self.assertTrue(Solution().isValidBST(root))

    def test_isValidBST2(self):
        root = build_tree([5, 1, 4, None, None, 3, 6])
        self.assertFalse(Solution().isValidBST(root))

    def test_isValidBST3(self):
        root = build_tree([1, 1])
        self.assertFalse(Solution().isValidBST(root))
