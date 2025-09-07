import unittest
from Solution0437 import Solution, TreeNode

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
    def test_path_sum(self):
        tree = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(Solution().pathSum(tree, 8), 3)

    def test_path_sum2(self):
        tree = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        self.assertEqual(Solution().pathSum(tree, 22), 3)
