# #Medium #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree
# #LeetCode_75_Binary_Tree/DFS #Level_2_Day_7_Tree #Big_O_Time_O(n)_Space_O(n)
# #2025_07_26_Time_0_ms_(100.00%)_Space_18.23_MB_(71.00%)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        def dfs(node: TreeNode, target_sum: int, curr_sum: int) -> None:
            if not node:
                return

            curr_sum += node.val
            self.count += self.prefix_sum.get(curr_sum - target_sum, 0)
            self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1
            dfs(node.left, target_sum, curr_sum)
            dfs(node.right, target_sum, curr_sum)

            self.prefix_sum[curr_sum] -= 1

        self.count = 0
        self.prefix_sum = {0: 1}
        dfs(root, target_sum, 0)
        return self.count
