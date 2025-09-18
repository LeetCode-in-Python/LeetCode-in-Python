# #Easy #Depth_First_Search #Tree #Binary_Search #Binary_Tree #Binary_Search_II_Day_10
# #Top_Interview_150_Binary_Tree_General #2025_09_17_Time_0_ms_(100.00%)_Space_23.29_MB_(82.07%)

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self._left_height(root)
        right_height = self._right_height(root)
        if left_height == right_height:
            return (1 << left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def _left_height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + self._left_height(node.left)

    def _right_height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + self._right_height(node.right)


