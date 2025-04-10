# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Two_Pointers #Linked_List
# #Algorithm_I_Day_5_Two_Pointers #Level_2_Day_3_Linked_List #Top_Interview_150_Linked_List
# #Big_O_Time_O(L)_Space_O(L) #2024_06_04_Time_21_ms_(99.70%)_Space_16.4_MB_(86.23%)

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
