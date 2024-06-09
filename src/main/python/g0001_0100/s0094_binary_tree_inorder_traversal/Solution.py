# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Depth_First_Search #Tree #Binary_Tree
# #Stack #Data_Structure_I_Day_10_Tree #Udemy_Tree_Stack_Queue #Big_O_Time_O(n)_Space_O(n)
# #2024_06_09_Time_28_ms_(91.67%)_Space_16.5_MB_(69.09%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
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

# Example usage:
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# sol = Solution()
# print(sol.inorderTraversal(root))  # Output: [1, 3, 2]
        