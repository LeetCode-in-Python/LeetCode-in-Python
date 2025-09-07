# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Depth_First_Search #Tree #Binary_Tree
# #Stack #Data_Structure_I_Day_10_Tree #Udemy_Tree_Stack_Queue #Big_O_Time_O(n)_Space_O(n)
# #2025_07_24_Time_0_ms_(100.00%)_Space_17.90_MB_(12.04%)

from typing import Optional, List

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
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        answer = []
        self._inorderTraversal(root, answer)
        return answer

    def _inorderTraversal(self, root, answer):
        if root is None:
            return
        if root.left is not None:
            self._inorderTraversal(root.left, answer)
        answer.append(root.val)
        if root.right is not None:
            self._inorderTraversal(root.right, answer)
