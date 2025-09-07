import unittest
from Solution0138 import Solution, Node

def build_list_with_random(values_and_randoms):
    if not values_and_randoms:
        return None
    
    # Create nodes
    nodes = []
    for val, _ in values_and_randoms:
        nodes.append(Node(val))
    
    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set random pointers
    for i, (_, random_idx) in enumerate(values_and_randoms):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
    
    return nodes[0]

def list_to_values(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class SolutionTest(unittest.TestCase):
    def test_copyRandomList(self):
        # [[7,None],[13,0],[11,4],[10,2],[1,0]]
        head = build_list_with_random([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
        result = Solution().copyRandomList(head)
        self.assertEqual(list_to_values(result), [7, 13, 11, 10, 1])

    def test_copyRandomList2(self):
        # [[1,1],[2,1]]
        head = build_list_with_random([(1, 1), (2, 1)])
        result = Solution().copyRandomList(head)
        self.assertEqual(list_to_values(result), [1, 2])

    def test_copyRandomList3(self):
        # [[3,None],[3,0],[3,None]]
        head = build_list_with_random([(3, None), (3, 0), (3, None)])
        result = Solution().copyRandomList(head)
        self.assertEqual(list_to_values(result), [3, 3, 3])
