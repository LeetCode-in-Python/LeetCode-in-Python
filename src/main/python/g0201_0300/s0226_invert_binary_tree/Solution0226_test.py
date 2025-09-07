import unittest
from Solution0226 import Solution, TreeNode

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

def to_list(root):
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
    while result and result[-1] is None:
        result.pop()
    return result

class SolutionTest(unittest.TestCase):
    def test_invertTree(self):
        root = build_tree([4,2,7,1,3,6,9])
        result = Solution().invertTree(root)
        self.assertEqual(to_list(result), [4,7,2,9,6,3,1])

    def test_invertTree2(self):
        root = build_tree([2,1,3])
        result = Solution().invertTree(root)
        self.assertEqual(to_list(result), [2,3,1])

    def test_invertTree3(self):
        root = build_tree([])
        result = Solution().invertTree(root)
        self.assertEqual(result, None)
