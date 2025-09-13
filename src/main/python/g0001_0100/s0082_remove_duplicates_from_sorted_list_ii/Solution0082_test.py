import unittest
from Solution0082 import Solution, ListNode

class SolutionTest(unittest.TestCase):
    def test_deleteDuplicates(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(4)
        head.next.next.next.next.next.next = ListNode(5)
        result = Solution().deleteDuplicates(head)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [1, 2, 5])

    def test_deleteDuplicates2(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(3)
        result = Solution().deleteDuplicates(head)
        # Convert to list for comparison
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
        self.assertEqual(result_list, [2, 3])
