import unittest
import importlib

mod = importlib.import_module('Solution0019')

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return ""

def construct_linked_list(values):
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
    def test_removeNthFromEnd(self):
        mod.ListNode = ListNode
        node1 = construct_linked_list([1, 2, 3, 4, 5])
        result = mod.Solution().removeNthFromEnd(node1, 2)
        self.assertEqual(to_string(result), "1, 2, 3, 5")

    def test_removeNthFromEnd2(self):
        mod.ListNode = ListNode
        node1 = ListNode(1)
        result = mod.Solution().removeNthFromEnd(node1, 1)
        self.assertIsNone(result)
