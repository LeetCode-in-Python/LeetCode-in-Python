import unittest
from Solution0142 import Solution, ListNode

def build_list_with_cycle(values, cycle_pos):
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if cycle_pos >= 0 and cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]
    
    return nodes[0]

class SolutionTest(unittest.TestCase):
    def test_detectCycle(self):
        head = build_list_with_cycle([3, 2, 0, -4], 1)
        result = Solution().detectCycle(head)
        self.assertEqual(result.val, 2)

    def test_detectCycle2(self):
        head = build_list_with_cycle([1, 2], 0)
        result = Solution().detectCycle(head)
        self.assertEqual(result.val, 1)

    def test_detectCycle3(self):
        head = build_list_with_cycle([1], -1)
        result = Solution().detectCycle(head)
        self.assertIsNone(result)
