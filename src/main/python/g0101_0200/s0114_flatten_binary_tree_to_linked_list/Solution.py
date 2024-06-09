# #Medium #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree #Stack #Linked_List
# #Udemy_Linked_List #Big_O_Time_O(N)_Space_O(N)
# #2024_06_09_Time_24_ms_(99.54%)_Space_16.7_MB_(86.32%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.find_tail(root)

    def find_tail(self, root: TreeNode) -> TreeNode:
        left = root.left
        right = root.right
        # Find the tail of the left subtree, tail means the most left leaf
        if left:
            tail = self.find_tail(left)
            # Stitch the right subtree below the tail
            root.left = None
            root.right = left
            tail.right = right
        else:
            tail = root
        # Find tail of the right subtree
        if tail.right is None:
            return tail
        else:
            return self.find_tail(tail.right)
