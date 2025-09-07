import unittest
from Solution0206 import Solution, ListNode

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
    def test_reverseList(self):
        head = from_list([1,2,3,4,5])
        result = Solution().reverseList(head)
        self.assertEqual(to_list(result), [5,4,3,2,1])

    def test_reverseList2(self):
        head = from_list([1,2])
        result = Solution().reverseList(head)
        self.assertEqual(to_list(result), [2,1])

    def test_reverseList3(self):
        head = from_list([])
        result = Solution().reverseList(head)
        self.assertEqual(to_list(result), [])
