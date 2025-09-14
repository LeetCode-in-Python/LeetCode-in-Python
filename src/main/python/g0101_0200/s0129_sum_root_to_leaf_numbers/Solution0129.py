# #Medium #Depth_First_Search #Tree #Binary_Tree #Top_Interview_150_Binary_Tree_General
# #2025_09_14_Time_0_ms_(100.00%)_Space_17.98_MB_(15.68%)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum_total = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self._recurseSum(root, 0)
        return self.sum_total

    def _recurseSum(self, node: Optional[TreeNode], cur_num: int):
        if node.left is None and node.right is None:
            self.sum_total += 10 * cur_num + node.val
        else:
            if node.left is not None:
                self._recurseSum(node.left, 10 * cur_num + node.val)
            if node.right is not None:
                self._recurseSum(node.right, 10 * cur_num + node.val)
