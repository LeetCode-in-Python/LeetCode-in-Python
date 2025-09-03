# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #Heap_Priority_Queue #Linked_List
# #Divide_and_Conquer #Merge_Sort #Top_Interview_150_Divide_and_Conquer
# #Big_O_Time_O(k*n*log(k))_Space_O(log(k)) #2025_07_22_Time_5_ms_(93.52%)_Space_20.28_MB_(55.14%)

from typing import List, Optional

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return ListNode().next
        else:
            cnt = 0
            n = len(lists)

            first = ListNode()
            temp = first
            while cnt < n:
                temp.next = lists[cnt]
                while temp.next is not None:
                    temp = temp.next
                cnt +=1
            return self.list_to_linked_list(self.linked_list_to_list(first.next))

    def linked_list_to_list(self,head):
        if head == None:
            return 
        else:
            l = []
            temp = head
            while temp is not None:
                l.append(temp.val)
                temp = temp.next
            return sorted(l)

    def list_to_linked_list(self,l):
        if l == None:
            return
        first = ListNode()
        temp = first
        for i in l:
            node = ListNode(i)
            temp.next = node
            temp = temp.next
        return first.next
