import unittest
from Solution0543 import Solution, TreeNode

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
    def test_diameterOfBinaryTree(self):
        self.assertEqual(Solution().diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])), 3)

    def test_diameterOfBinaryTree2(self):
        self.assertEqual(Solution().diameterOfBinaryTree(build_tree([1, 2])), 1)
