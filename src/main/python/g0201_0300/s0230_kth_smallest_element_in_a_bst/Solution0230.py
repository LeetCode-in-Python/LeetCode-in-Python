# #Medium #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree #Binary_Search_Tree
# #Data_Structure_II_Day_17_Tree #Level_2_Day_9_Binary_Search_Tree
# #Top_Interview_150_Binary_Search_Tree #Big_O_Time_O(n)_Space_O(n)
# #2025_07_25_Time_0_ms_(100.00%)_Space_21.13_MB_(27.27%)

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
