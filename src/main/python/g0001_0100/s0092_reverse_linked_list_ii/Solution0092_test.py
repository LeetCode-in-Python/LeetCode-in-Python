import unittest
from Solution0092 import Solution, ListNode

class SolutionTest(unittest.TestCase):
    def test_reverseBetween(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        result = Solution().reverseBetween(head, 2, 4)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [1, 4, 3, 2, 5])

    def test_reverseBetween2(self):
        head = ListNode(5)
        result = Solution().reverseBetween(head, 1, 1)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [5])
