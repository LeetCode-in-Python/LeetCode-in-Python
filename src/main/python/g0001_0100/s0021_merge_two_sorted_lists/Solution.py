# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Linked_List #Recursion
# #Data_Structure_I_Day_7_Linked_List #Algorithm_I_Day_10_Recursion_Backtracking
# #Level_1_Day_3_Linked_List #Udemy_Linked_List #Big_O_Time_O(m+n)_Space_O(m+n)
# #2024_06_04_Time_31_ms_(92.02%)_Space_16.5_MB_(51.91%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        current = dummy
        
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    current.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    current.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1 is not None:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next
            
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst
        