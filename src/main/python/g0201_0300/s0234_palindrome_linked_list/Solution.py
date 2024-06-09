# #Easy #Top_100_Liked_Questions #Two_Pointers #Stack #Linked_List #Recursion
# #Level_2_Day_3_Linked_List #Udemy_Linked_List #Big_O_Time_O(n)_Space_O(1)
# #2024_06_09_Time_282_ms_(75.97%)_Space_31.9_MB_(83.09%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Calculate the length of the linked list
        length = 0
        right = head
        while right:
            right = right.next
            length += 1
        
        # Reverse the right half of the list
        length //= 2
        right = head
        for _ in range(length):
            right = right.next
        
        prev = None
        while right:
            next_node = right.next
            right.next = prev
            prev = right
            right = next_node
        
        # Compare the left half and the right half
        for _ in range(length):
            if head and prev and head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
        return True
