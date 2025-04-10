# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Math #Linked_List #Recursion
# #Data_Structure_II_Day_10_Linked_List #Programming_Skills_II_Day_15
# #Top_Interview_150_Linked_List #Big_O_Time_O(max(N,M))_Space_O(max(N,M))
# #AI_can_be_used_to_solve_the_task #2024_06_06_Time_47_ms_(90.77%)_Space_16.6_MB_(83.79%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        p, q, curr = l1, l2, dummy_head
        carry = 0
        
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy_head.next
