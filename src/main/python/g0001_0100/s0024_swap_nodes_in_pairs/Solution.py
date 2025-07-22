# #Medium #Top_100_Liked_Questions #Linked_List #Recursion #Data_Structure_II_Day_12_Linked_List
# #Udemy_Linked_List #Big_O_Time_O(n)_Space_O(1)
# #2025_07_22_Time_0_ms_(100.00%)_Space_17.66_MB_(83.09%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  
            return head  
        nxt = head.next

        head.next = self.swapPairs(nxt.next)  
        nxt.next = head

        return nxt
