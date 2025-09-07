# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Linked_List #Recursion
# #LeetCode_75_LinkedList #Data_Structure_I_Day_8_Linked_List
# #Algorithm_I_Day_10_Recursion_Backtracking #Level_1_Day_3_Linked_List #Udemy_Linked_List
# #Big_O_Time_O(N)_Space_O(1) #2025_07_25_Time_0_ms_(100.00%)_Space_18.75_MB_(37.87%)

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
