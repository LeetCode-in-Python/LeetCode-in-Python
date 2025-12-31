# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Depth_First_Search #Breadth_First_Search
# #Tree #Binary_Tree #Data_Structure_I_Day_11_Tree #Level_2_Day_15_Tree
# #Top_Interview_150_Binary_Tree_General #Big_O_Time_O(N)_Space_O(log(N))
# #2025_07_24_Time_0_ms_(100.00%)_Space_17.74_MB_(83.76%)

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left_node: TreeNode, right_node: TreeNode) -> bool:
        if left_node is None or right_node is None:
            return left_node is None and right_node is None
        if left_node.val != right_node.val:
            return False
        return self.helper(left_node.left, right_node.right) and self.helper(left_node.right, right_node.left)
