# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Hash_Table #Two_Pointers #Linked_List
# #Data_Structure_I_Day_7_Linked_List #Udemy_Linked_List #Top_Interview_150_Linked_List
# #Big_O_Time_O(N)_Space_O(1) #2025_07_25_Time_44_ms_(80.06%)_Space_19.98_MB_(29.66%)

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
