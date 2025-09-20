# #Easy #Depth_First_Search #Breadth_First_Search #Tree #Binary_Tree #Binary_Search_Tree
# #Top_Interview_150_Binary_Search_Tree #2025_09_20_Time_3_ms_(77.28%)_Space_19.64_MB_(47.96%)

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.prev = float('inf')
        
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            self.ans = min(self.ans, abs(node.val - self.prev))
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.ans
