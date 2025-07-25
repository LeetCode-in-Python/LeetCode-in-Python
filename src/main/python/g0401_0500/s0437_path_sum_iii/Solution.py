# #Medium #Top_100_Liked_Questions #Depth_First_Search #Tree #Binary_Tree
# #LeetCode_75_Binary_Tree/DFS #Level_2_Day_7_Tree #Big_O_Time_O(n)_Space_O(n)
# #2025_07_25_Time_6_ms_(68.63%)_Space_18.23_MB_(71.08%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node: TreeNode, targetSum: int, curr_sum: int) -> None:
            if not node:
                return

            curr_sum += node.val
            self.count += self.prefix_sum.get(curr_sum - targetSum, 0)
            self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1
            dfs(node.left, targetSum, curr_sum)
            dfs(node.right, targetSum, curr_sum)

            self.prefix_sum[curr_sum] -= 1

        self.count = 0
        self.prefix_sum = {0: 1}
        dfs(root, targetSum, 0)
        return self.count
