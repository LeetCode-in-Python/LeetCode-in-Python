# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #Dynamic_Programming #Depth_First_Search
# #Tree #Binary_Tree #Udemy_Tree_Stack_Queue #Big_O_Time_O(N)_Space_O(N)
# #2024_06_09_Time_57_ms_(86.71%)_Space_20.9_MB_(40.96%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.max_sum

    def helper(self, root):
        if not root:
            return 0
        
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        
        current = root.val + left + right
        self.max_sum = max(self.max_sum, current)
        
        return root.val + max(left, right)

        