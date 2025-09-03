import unittest
import importlib

mod = importlib.import_module('Solution0024')


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
    def test_swapPairs(self):
        mod.ListNode = ListNode
        head = from_list([1, 2, 3, 4])
        result = mod.Solution().swapPairs(head)
        self.assertEqual(to_string(result), "2, 1, 4, 3")

    def test_swapPairs2(self):
        mod.ListNode = ListNode
        result = mod.Solution().swapPairs(ListNode(1))
        self.assertEqual(to_string(result), "1") 