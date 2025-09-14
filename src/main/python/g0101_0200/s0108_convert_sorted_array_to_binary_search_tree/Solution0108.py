# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Tree #Binary_Tree
# #Binary_Search_Tree #Divide_and_Conquer #Data_Structure_II_Day_15_Tree
# #Level_2_Day_9_Binary_Search_Tree #Udemy_Tree_Stack_Queue #Top_Interview_150_Divide_and_Conquer
# #2025_09_14_Time_0_ms_(100.00%)_Space_19.29_MB_(18.53%)

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Set up recursion
        return self._makeTree(nums, 0, len(nums) - 1)

    def _makeTree(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        # left as lowest# can't be greater than right
        if left > right:
            return None
        # Set median# as node
        mid = (left + right) // 2
        mid_node = TreeNode(nums[mid])
        # Set mid node's kids
        mid_node.left = self._makeTree(nums, left, mid - 1)
        mid_node.right = self._makeTree(nums, mid + 1, right)
        # Sends node back || Goes back to prev node
        return mid_node
