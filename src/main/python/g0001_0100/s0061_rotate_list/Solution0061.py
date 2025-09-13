# #Medium #Two_Pointers #Linked_List #Programming_Skills_II_Day_16 #Udemy_Linked_List
# #Top_Interview_150_Linked_List #2025_09_13_Time_0_ms_(100.00%)_Space_12.50_MB_(74.08%)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        tail = head
        # find the count and let tail points to last node
        count = 1
        while tail is not None and tail.next is not None:
            count += 1
            tail = tail.next
        # calculate number of times to rotate by count modulas
        times = k % count
        if times == 0:
            return head
        temp = head
        # iterate and go to the K+1 th node from the end or count - K - 1 node from start
        for i in range(1, count - times):
            if temp is not None:
                temp = temp.next
        new_head = None
        if temp is not None and tail is not None:
            new_head = temp.next
            temp.next = None
            tail.next = head
        return new_head
