# #Medium #Two_Pointers #Linked_List #Data_Structure_II_Day_11_Linked_List
# #Algorithm_II_Day_3_Two_Pointers #Top_Interview_150_Linked_List
# #2025_09_13_Time_0_ms_(100.00%)_Space_17.98_MB_(25.97%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        curr = head.next
        while curr is not None:
            flag_found_duplicate = False
            while curr is not None and prev.next.val == curr.val:
                flag_found_duplicate = True
                curr = curr.next
            if flag_found_duplicate:
                prev.next = curr
                if curr is not None:
                    curr = curr.next
            else:
                prev = prev.next
                prev.next = curr
                curr = curr.next
        return dummy.next
