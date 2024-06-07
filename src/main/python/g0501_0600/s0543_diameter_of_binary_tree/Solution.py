# #Easy #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree #Level_2_Day_7_Tree
# #Udemy_Tree_Stack_Queue #Big_O_Time_O(n)_Space_O(n)
# #2024_06_07_Time_51_ms_(36.84%)_Space_19.2_MB_(86.39%)

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
        leftLength = 1 + self.diameterOfBinaryTreeUtil(root.left) if root.left else 0
        rightLength = 1 + self.diameterOfBinaryTreeUtil(root.right) if root.right else 0
        self.diameter = max(self.diameter, leftLength + rightLength)
        return max(leftLength, rightLength)
