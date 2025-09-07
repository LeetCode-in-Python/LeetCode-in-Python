import unittest
from Solution0230 import Solution, TreeNode

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
    def test_kthSmallest(self):
        root = build_tree([3,1,4,None,2])
        self.assertEqual(Solution().kthSmallest(root, 1), 1)

    def test_kthSmallest2(self):
        root = build_tree([5,3,6,2,4,None,None,1])
        self.assertEqual(Solution().kthSmallest(root, 3), 3)
