# #Medium #Two_Pointers #Linked_List #Top_Interview_150_Linked_List
# #2025_09_13_Time_0_ms_(100.00%)_Space_17.98_MB_(21.24%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        n_head = ListNode(0)
        n_tail = ListNode(0)
        ptr = n_tail
        temp = n_head
        while head is not None:
            n_next = head.next
            if head.val < x:
                n_head.next = head
                n_head = n_head.next
            else:
                n_tail.next = head
                n_tail = n_tail.next
            head = n_next
        n_tail.next = None
        n_head.next = ptr.next
        return temp.next
