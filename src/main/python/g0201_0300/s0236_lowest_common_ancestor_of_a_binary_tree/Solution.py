# #Medium #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree
# #LeetCode_75_Binary_Tree/DFS #Data_Structure_II_Day_18_Tree #Udemy_Tree_Stack_Queue
# #Top_Interview_150_Binary_Tree_General #Big_O_Time_O(n)_Space_O(n)
# #2024_06_09_Time_43_ms_(89.34%)_Space_21_MB_(44.04%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        return right
