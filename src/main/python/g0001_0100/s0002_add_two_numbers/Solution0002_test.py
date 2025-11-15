import unittest
from Solution0002 import Solution, ListNode

def construct_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_str(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    return ', '.join(vals)

class SolutionTest(unittest.TestCase):
    def test_addTwoNumbers(self):
        list_node1 = construct_linked_list([2, 4, 3])
        list_node2 = construct_linked_list([5, 6, 4])
        result = Solution().addTwoNumbers(list_node1, list_node2)
        self.assertEqual(linked_list_to_str(result), "7, 0, 8")

    def test_addTwoNumbers2(self):
        list_node1 = ListNode(0)
        list_node2 = ListNode(0)
        result = Solution().addTwoNumbers(list_node1, list_node2)
        self.assertEqual(linked_list_to_str(result), "0")

    def test_addTwoNumbers3(self):
        list_node1 = construct_linked_list([9, 9, 9, 9, 9, 9, 9])
        list_node2 = construct_linked_list([9, 9, 9, 9])
        result = Solution().addTwoNumbers(list_node1, list_node2)
        self.assertEqual(linked_list_to_str(result), "8, 9, 9, 9, 0, 0, 0, 1")
