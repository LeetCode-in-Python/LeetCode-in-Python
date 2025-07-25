# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Sorting #Two_Pointers #Linked_List
# #Divide_and_Conquer #Merge_Sort #Level_2_Day_4_Linked_List #Top_Interview_150_Divide_and_Conquer
# #Big_O_Time_O(log(N))_Space_O(log(N)) #2025_07_25_Time_186_ms_(43.67%)_Space_32.96_MB_(41.09%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the middle of the list
        slow, fast = head, head
        pre = slow
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        # Sort the two halves
        first = self.sortList(head)
        second = self.sortList(slow)

        # Merge the sorted halves
        res = ListNode(0)
        cur = res
        while first or second:
            if not first:
                cur.next = second
                break
            elif not second:
                cur.next = first
                break
            elif first.val <= second.val:
                cur.next = first
                first = first.next
                cur = cur.next
            else:
                cur.next = second
                second = second.next
                cur = cur.next

        return res.next
