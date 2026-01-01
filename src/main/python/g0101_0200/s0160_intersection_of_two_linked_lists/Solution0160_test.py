import unittest
from Solution0160 import Solution, ListNode

def build_intersecting_lists(list_a, list_b, skip_a, skip_b):
    if not list_a or not list_b:
        return None, None
    
    nodes_a = [ListNode(val) for val in list_a]
    nodes_b = [ListNode(val) for val in list_b]
    
    # Connect listA
    for i in range(len(nodes_a) - 1):
        nodes_a[i].next = nodes_a[i + 1]
    
    # Connect listB
    for i in range(len(nodes_b) - 1):
        nodes_b[i].next = nodes_b[i + 1]
    
    # Create intersection
    if skip_a < len(nodes_a) and skip_b < len(nodes_b):
        nodes_b[-1].next = nodes_a[skip_a]
    
    return nodes_a[0], nodes_b[0]

class SolutionTest(unittest.TestCase):
    def test_getIntersectionNode(self):
        # listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
        head_a, head_b = build_intersecting_lists([4,1,8,4,5], [5,6,1,8,4,5], 2, 3)
        result = Solution().getIntersectionNode(head_a, head_b)
        self.assertEqual(result.val, 8)

    def test_getIntersectionNode2(self):
        # listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
        head_a, head_b = build_intersecting_lists([1,9,1,2,4], [3,2,4], 3, 1)
        result = Solution().getIntersectionNode(head_a, head_b)
        self.assertEqual(result.val, 2)

    def test_getIntersectionNode3(self):
        # listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
        head_a, head_b = build_intersecting_lists([2,6,4], [1,5], 3, 2)
        result = Solution().getIntersectionNode(head_a, head_b)
        self.assertIsNone(result)
