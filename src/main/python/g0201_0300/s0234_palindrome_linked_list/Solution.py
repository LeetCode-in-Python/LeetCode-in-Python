# #Easy #Top_100_Liked_Questions #Two_Pointers #Stack #Linked_List #Recursion
# #Level_2_Day_3_Linked_List #Udemy_Linked_List #Big_O_Time_O(n)_Space_O(1)
# #2025_07_25_Time_23_ms_(81.92%)_Space_39.40_MB_(37.99%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        l = 0
        r = len(arr) -1 
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l+=1
            r-=1
        return True
