# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Hash_Table #Two_Pointers #Linked_List
# #Data_Structure_II_Day_11_Linked_List #Udemy_Linked_List #Big_O_Time_O(M+N)_Space_O(1)
# #2025_07_25_Time_83_ms_(67.29%)_Space_27.89_MB_(40.40%)

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = headB if node1 is None else node1.next
            node2 = headA if node2 is None else node2.next
        return node1
