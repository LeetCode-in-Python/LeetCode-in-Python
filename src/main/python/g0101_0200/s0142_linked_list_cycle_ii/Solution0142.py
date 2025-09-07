# #Medium #Top_100_Liked_Questions #Hash_Table #Two_Pointers #Linked_List
# #Data_Structure_II_Day_10_Linked_List #Level_1_Day_4_Linked_List #Udemy_Linked_List
# #Big_O_Time_O(N)_Space_O(1) #2025_07_25_Time_38_ms_(94.15%)_Space_19.60_MB_(79.86%)

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
