import unittest
import importlib

mod = importlib.import_module('Solution0023')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def test_mergeKLists(self):
        mod.ListNode = ListNode
        head1 = from_list([1, 4, 5])
        head2 = from_list([1, 3, 4])
        head3 = from_list([2, 6])
        result = mod.Solution().mergeKLists([head1, head2, head3])
        self.assertEqual(to_string(result), "1, 1, 2, 3, 4, 4, 5, 6")

    def test_mergeKLists2(self):
        mod.ListNode = ListNode
        head1 = from_list([1, 3, 5, 7, 11])
        head2 = from_list([2, 8, 12])
        head3 = from_list([4, 6, 9, 10])
        result = mod.Solution().mergeKLists([head1, head2, head3])
        self.assertEqual(to_string(result), "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12") 