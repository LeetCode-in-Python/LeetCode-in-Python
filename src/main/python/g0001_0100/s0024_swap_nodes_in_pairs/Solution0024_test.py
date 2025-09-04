import unittest
from Solution0024 import Solution, ListNode

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
        head = from_list([1, 2, 3, 4])
        result = Solution().swapPairs(head)
        self.assertEqual(to_string(result), "2, 1, 4, 3")

    def test_swapPairs2(self):
        result = Solution().swapPairs(ListNode(1))
        self.assertEqual(to_string(result), "1")
