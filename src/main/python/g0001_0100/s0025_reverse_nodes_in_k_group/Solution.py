# #Hard #Top_100_Liked_Questions #Linked_List #Recursion #Data_Structure_II_Day_13_Linked_List
# #Udemy_Linked_List #Top_Interview_150_Linked_List #Big_O_Time_O(n)_Space_O(k)
# #2024_06_04_Time_36_ms_(90.51%)_Space_17.3_MB_(94.94%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 1:
            return head

        j = 0
        length = head
        # Loop for checking the length of the linked list, if the linked list is less than k, then return it as it is.
        while j < k:
            if length is None:
                return head
            length = length.next
            j += 1

        # Reverse linked list logic applied here.
        current = head
        next_node = None
        prev = None
        i = 0
        # Traverse the while loop for k times to reverse the node in k groups.
        while i != k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            i += 1

        # 'head' is now pointing to the first node of k group, which is now going to point to the next k group linked list.
        # Recursion for further remaining linked list.
        head.next = self.reverseKGroup(current, k)
        return prev
