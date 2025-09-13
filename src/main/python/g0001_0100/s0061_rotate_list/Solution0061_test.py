import unittest
from Solution0061 import Solution, ListNode

class SolutionTest(unittest.TestCase):
    def test_rotateRight(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        result = Solution().rotateRight(head, 2)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [4, 5, 1, 2, 3])

    def test_rotateRight2(self):
        head = ListNode(0)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        result = Solution().rotateRight(head, 4)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [2, 0, 1])
