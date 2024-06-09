# #Medium #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree #Binary_Search_Tree
# #Data_Structure_II_Day_17_Tree #Level_2_Day_9_Binary_Search_Tree #Big_O_Time_O(n)_Space_O(n)
# #2024_06_09_Time_44_ms_(61.91%)_Space_19.4_MB_(88.66%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.k = 0
        self.count = 0
        self.val = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.count = 0
        self.val = None
        self.calculate(root)
        return self.val

    def calculate(self, node):
        if not node:
            return

        if node.left:
            self.calculate(node.left)

        self.count += 1
        if self.count == self.k:
            self.val = node.val
            return

        if node.right:
            self.calculate(node.right)
