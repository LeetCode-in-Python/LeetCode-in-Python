# #Medium #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree
# #LeetCode_75_Binary_Tree/DFS #Data_Structure_II_Day_18_Tree #Udemy_Tree_Stack_Queue
# #Top_Interview_150_Binary_Tree_General #Big_O_Time_O(n)_Space_O(n)
# #2025_07_25_Time_41_ms_(97.74%)_Space_22.14_MB_(43.54%)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
