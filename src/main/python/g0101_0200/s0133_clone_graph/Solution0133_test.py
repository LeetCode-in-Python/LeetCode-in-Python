import unittest
from Solution0133 import Solution, Node

class SolutionTest(unittest.TestCase):
    def test_cloneGraph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        
        result = Solution().cloneGraph(node1)
        
        # Check that the cloned graph has the same structure
        self.assertEqual(result.val, 1)
        self.assertEqual(len(result.neighbors), 2)
        self.assertEqual(result.neighbors[0].val, 2)
        self.assertEqual(result.neighbors[1].val, 4)

    def test_cloneGraph2(self):
        node1 = Node(1)
        result = Solution().cloneGraph(node1)
        self.assertEqual(result.val, 1)
        self.assertEqual(len(result.neighbors), 0)

    def test_cloneGraph3(self):
        self.assertIsNone(Solution().cloneGraph(None))
