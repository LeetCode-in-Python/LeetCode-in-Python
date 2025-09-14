# #Medium #Top_100_Liked_Questions #Depth_First_Search #Breadth_First_Search #Tree #Binary_Tree
# #LeetCode_75_Binary_Tree/BFS #Data_Structure_II_Day_16_Tree #Level_2_Day_15_Tree
# #Top_Interview_150_Binary_Tree_BFS #2025_09_14_Time_0_ms_(100.00%)_Space_17.76_MB_(60.72%)

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._recurse(root, 0, result)
        return result

    def _recurse(self, node: Optional[TreeNode], level: int, result: List[int]):
        if node is not None:
            if len(result) < level + 1:
                result.append(node.val)
            self._recurse(node.right, level + 1, result)
            self._recurse(node.left, level + 1, result)

