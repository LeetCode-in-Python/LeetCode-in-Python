# #Easy #Depth_First_Search #Breadth_First_Search #Tree #Binary_Tree #Level_2_Day_15_Tree
# #Udemy_Tree_Stack_Queue #Top_Interview_150_Binary_Tree_General
# #2025_09_13_Time_0_ms_(100.00%)_Space_17.70_MB_(65.76%)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is None and q is None
        b1 = self.isSameTree(p.left, q.left)
        b2 = self.isSameTree(p.right, q.right)
        return p.val == q.val and b1 and b2
