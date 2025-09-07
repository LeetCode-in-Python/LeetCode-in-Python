import unittest
from Solution0148 import Solution, ListNode

def from_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head):
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result

class SolutionTest(unittest.TestCase):
    def test_sortList(self):
        head = from_list([4, 2, 1, 3])
        result = Solution().sortList(head)
        self.assertEqual(to_list(result), [1, 2, 3, 4])

    def test_sortList2(self):
        head = from_list([-1, 5, 3, 4, 0])
        result = Solution().sortList(head)
        self.assertEqual(to_list(result), [-1, 0, 3, 4, 5])

    def test_sortList3(self):
        head = from_list([])
        result = Solution().sortList(head)
        self.assertEqual(to_list(result), [])
