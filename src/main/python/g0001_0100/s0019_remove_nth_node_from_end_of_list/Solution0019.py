# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Two_Pointers #Linked_List
# #Algorithm_I_Day_5_Two_Pointers #Level_2_Day_3_Linked_List #Top_Interview_150_Linked_List
# #Big_O_Time_O(L)_Space_O(L) #2025_07_22_Time_0_ms_(100.00%)_Space_17.70_MB_(84.76%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.n = n
        dummy = ListNode(0, head)
        self._removeNth(dummy)
        return dummy.next

    def _removeNth(self, node):
        if not node.next:
            return
        
        self._removeNth(node.next)
        self.n -= 1
        
        if self.n == 0:
            node.next = node.next.next
