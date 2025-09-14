import unittest
from Solution0117 import Solution, Node

class SolutionTest(unittest.TestCase):
    def test_connect(self):
        self.assertIsNone(Solution().connect(None))

    def test_connect2(self):
        node = Node(1)
        node.left = Node(2)
        node.left.left = Node(4)
        node.left.right = Node(5)
        node.right = Node(3)
        node.right.right = Node(7)

        result = Solution().connect(node)
        
        # Check that next pointers are set correctly
        self.assertEqual(result.left.next.val, 3)
        self.assertEqual(result.left.left.next.val, 5)
        self.assertEqual(result.left.right.next.val, 7)
        self.assertIsNone(result.right.next)

    def test_connect3(self):
        node = Node(1)
        node.left = Node(2)
        node.left.left = Node(4)
        node.left.left.left = Node(7)
        node.left.right = Node(5)
        node.right = Node(3)
        node.right.right = Node(6)
        node.right.right.right = Node(8)

        result = Solution().connect(node)
        
        # Check that next pointers are set correctly
        self.assertEqual(result.left.next.val, 3)
        self.assertEqual(result.left.left.next.val, 5)
        self.assertEqual(result.left.right.next.val, 6)
        self.assertEqual(result.left.left.left.next.val, 8)
        self.assertIsNone(result.right.next)
