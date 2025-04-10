# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Linked_List #Recursion
# #Data_Structure_I_Day_7_Linked_List #Algorithm_I_Day_10_Recursion_Backtracking
# #Level_1_Day_3_Linked_List #Udemy_Linked_List #Top_Interview_150_Linked_List
# #Big_O_Time_O(m+n)_Space_O(m+n) #2024_06_04_Time_31_ms_(92.02%)_Space_16.5_MB_(51.91%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        
        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    current.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    current.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1 is not None:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
            
        return dummy.next
