import unittest
from Solution0021 import Solution, ListNode

def from_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_string(head):
    parts = []
    curr = head
    while curr is not None:
        parts.append(str(curr.val))
        curr = curr.next
    return ", ".join(parts)

class SolutionTest(unittest.TestCase):
    def test_mergeTwoLists(self):
        l1 = from_list([1, 2, 4])
        l2 = from_list([1, 3, 4])
        self.assertEqual(to_string(Solution().mergeTwoLists(l1, l2)), "1, 1, 2, 3, 4, 4")

    def test_mergeTwoLists2(self):
        self.assertEqual(to_string(Solution().mergeTwoLists(ListNode(0), ListNode(0))), "0, 0") 
