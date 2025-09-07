import unittest
from Solution0234 import Solution, ListNode

def from_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

class SolutionTest(unittest.TestCase):
    def test_isPalindrome(self):
        head = from_list([1,2,2,1])
        self.assertTrue(Solution().isPalindrome(head))

    def test_isPalindrome2(self):
        head = from_list([1,2])
        self.assertFalse(Solution().isPalindrome(head))

    def test_isPalindrome3(self):
        head = from_list([1])
        self.assertTrue(Solution().isPalindrome(head))
