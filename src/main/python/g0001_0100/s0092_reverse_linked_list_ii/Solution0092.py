# #Medium #Linked_List #Top_Interview_150_Linked_List
# #2025_09_13_Time_0_ms_(100.00%)_Space_18.11_MB_(14.44%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        prev = None
        temp = head
        start = None
        k = left
        while temp is not None and k > 1:
            prev = temp
            temp = temp.next
            k -= 1
        if left > 1 and prev is not None:
            prev.next = None
        prev1 = None
        start = temp
        while temp is not None and right - left >= 0:
            prev1 = temp
            temp = temp.next
            right -= 1
        if prev1 is not None:
            prev1.next = None
        if left > 1 and prev is not None:
            prev.next = self._reverse(start)
        else:
            head = self._reverse(start)
            prev = head
        while prev.next is not None:
            prev = prev.next
        prev.next = temp
        return head

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        r = None
        while p is not None:
            q = p.next
            p.next = r
            r = p
            p = q
        return r
