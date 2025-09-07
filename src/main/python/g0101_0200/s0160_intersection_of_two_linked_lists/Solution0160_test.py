import unittest
from Solution0160 import Solution, ListNode

def build_intersecting_lists(listA, listB, skipA, skipB):
    if not listA or not listB:
        return None, None
    
    nodesA = [ListNode(val) for val in listA]
    nodesB = [ListNode(val) for val in listB]
    
    # Connect listA
    for i in range(len(nodesA) - 1):
        nodesA[i].next = nodesA[i + 1]
    
    # Connect listB
    for i in range(len(nodesB) - 1):
        nodesB[i].next = nodesB[i + 1]
    
    # Create intersection
    if skipA < len(nodesA) and skipB < len(nodesB):
        nodesB[-1].next = nodesA[skipA]
    
    return nodesA[0], nodesB[0]

class SolutionTest(unittest.TestCase):
    def test_getIntersectionNode(self):
        # listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
        headA, headB = build_intersecting_lists([4,1,8,4,5], [5,6,1,8,4,5], 2, 3)
        result = Solution().getIntersectionNode(headA, headB)
        self.assertEqual(result.val, 8)

    def test_getIntersectionNode2(self):
        # listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
        headA, headB = build_intersecting_lists([1,9,1,2,4], [3,2,4], 3, 1)
        result = Solution().getIntersectionNode(headA, headB)
        self.assertEqual(result.val, 2)

    def test_getIntersectionNode3(self):
        # listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
        headA, headB = build_intersecting_lists([2,6,4], [1,5], 3, 2)
        result = Solution().getIntersectionNode(headA, headB)
        self.assertIsNone(result)
