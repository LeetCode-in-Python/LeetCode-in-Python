# #Easy #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree #Level_2_Day_7_Tree
# #Udemy_Tree_Stack_Queue #Big_O_Time_O(n)_Space_O(n)
# #2025_07_25_Time_3_ms_(94.30%)_Space_20.69_MB_(95.89%)

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
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.diameterOfBinaryTreeUtil(root)
        return self.diameter

    def diameterOfBinaryTreeUtil(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_length = 1 + self.diameterOfBinaryTreeUtil(root.left) if root.left else 0
        right_length = 1 + self.diameterOfBinaryTreeUtil(root.right) if root.right else 0
        self.diameter = max(self.diameter, left_length + right_length)
        return max(left_length, right_length)
