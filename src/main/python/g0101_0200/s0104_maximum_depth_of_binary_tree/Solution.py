# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Depth_First_Search #Breadth_First_Search
# #Tree #Binary_Tree #LeetCode_75_Binary_Tree/DFS #Data_Structure_I_Day_11_Tree
# #Programming_Skills_I_Day_10_Linked_List_and_Tree #Udemy_Tree_Stack_Queue
# #Top_Interview_150_Binary_Tree_General #Big_O_Time_O(N)_Space_O(H)
# #2024_06_09_Time_35_ms_(85.47%)_Space_17.6_MB_(77.94%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right),
        )
