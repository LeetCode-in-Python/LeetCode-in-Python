# #Medium #Depth_First_Search #Breadth_First_Search #Tree #Binary_Tree #Linked_List
# #Algorithm_II_Day_7_Breadth_First_Search_Depth_First_Search
# #Top_Interview_150_Binary_Tree_General #2025_09_14_Time_44_ms_(70.94%)_Space_18.86_MB_(58.51%)

from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if root.left is not None:
            if root.right is not None:
                root.left.next = root.right
            elif root.next is not None:
                root.left.next = self._adjacentRightNode(root.next)
        if root.right is not None:
            root.right.next = self._adjacentRightNode(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root

    def _adjacentRightNode(self, root: Optional[Node]) -> Optional[Node]:
        temp = root
        while temp is not None:
            if temp.left is None and temp.right is None:
                temp = temp.next
            else:
                if temp.left is not None:
                    return temp.left
                if temp.right is not None:
                    return temp.right
        return None
