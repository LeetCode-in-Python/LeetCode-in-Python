# #Medium #Tree #Binary_Tree #Stack #Design #Binary_Search_Tree #Iterator
# #Data_Structure_II_Day_17_Tree #Programming_Skills_II_Day_16 #Level_2_Day_9_Binary_Search_Tree
# #Top_Interview_150_Binary_Tree_General #2025_09_14_Time_2_ms_(92.39%)_Space_25.20_MB_(18.38%)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        # Push all left children
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        # Smallest available node
        node = self.stack.pop()
        # If node has a right child → push its left subtree
        if node.right:
            self._push_left(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
