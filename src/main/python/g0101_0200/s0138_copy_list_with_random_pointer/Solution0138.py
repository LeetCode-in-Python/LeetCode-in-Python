# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Hash_Table #Linked_List
# #Programming_Skills_II_Day_14 #Udemy_Linked_List #Top_Interview_150_Linked_List
# #Big_O_Time_O(N)_Space_O(N) #2025_07_25_Time_38_ms_(77.31%)_Space_18.72_MB_(18.76%)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # First pass: create the cloned nodes and insert them right after the original nodes
        curr = head
        while curr:
            cloned_node = Node(curr.val)
            cloned_node.next = curr.next
            curr.next = cloned_node
            curr = cloned_node.next
        
        # Second pass: update the random pointers of the cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Third pass: separate the cloned list from the original list
        curr = head
        new_head = head.next
        while curr:
            cloned_node = curr.next
            curr.next = cloned_node.next
            if cloned_node.next:
                cloned_node.next = cloned_node.next.next
            curr = curr.next
        
        return new_head
