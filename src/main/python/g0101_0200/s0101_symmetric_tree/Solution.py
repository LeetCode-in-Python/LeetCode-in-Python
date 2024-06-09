# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Depth_First_Search #Breadth_First_Search
# #Tree #Binary_Tree #Data_Structure_I_Day_11_Tree #Level_2_Day_15_Tree
# #Big_O_Time_O(N)_Space_O(log(N)) #2024_06_09_Time_35_ms_(71.46%)_Space_16.6_MB_(14.05%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, leftNode: TreeNode, rightNode: TreeNode) -> bool:
        if leftNode is None or rightNode is None:
            return leftNode is None and rightNode is None
        if leftNode.val != rightNode.val:
            return False
        return self.helper(leftNode.left, rightNode.right) and self.helper(leftNode.right, rightNode.left)
        