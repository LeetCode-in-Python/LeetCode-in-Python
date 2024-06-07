# #Medium #Depth_First_Search #Tree #Binary_Tree #Level_2_Day_7_Tree #Big_O_Time_O(n)_Space_O(n)
# #2024_06_07_Time_264_ms_(30.25%)_Space_16.8_MB_(98.67%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.helper(root, targetSum, 0)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.count

    def helper(self, node: TreeNode, targetSum: int, currSum: int) -> None:
        if node is None:
            return
        currSum += node.val
        if targetSum == currSum:
            self.count += 1
        if node.left is not None:
            self.helper(node.left, targetSum, currSum)
        if node.right is not None:
            self.helper(node.right, targetSum, currSum)
        