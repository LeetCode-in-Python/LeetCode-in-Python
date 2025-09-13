import unittest
from Solution0086 import Solution, ListNode

class SolutionTest(unittest.TestCase):
    def test_partition(self):
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)
        result = Solution().partition(head, 3)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [1, 2, 2, 4, 3, 5])

    def test_partition2(self):
        head = ListNode(2)
        head.next = ListNode(1)
        result = Solution().partition(head, 2)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [1, 2])
