# #Medium #Array #Hash_Table #Tree #Binary_Tree #Divide_and_Conquer
# #Top_Interview_150_Binary_Tree_General #2025_09_14_Time_0_ms_(100.00%)_Space_19.02_MB_(96.74%)

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_index = [len(inorder) - 1]
        post_index = [len(postorder) - 1]
        return self._helper(inorder, postorder, in_index, post_index, float('inf'))

    def _helper(self, inorder: List[int], postorder: List[int], index: List[int], p_index: List[int], target: float) -> Optional[TreeNode]:
        if index[0] < 0 or (index[0] < len(inorder) and inorder[index[0]] == target):
            return None
        root = TreeNode(postorder[p_index[0]])
        p_index[0] -= 1
        root.right = self._helper(inorder, postorder, index, p_index, root.val)
        index[0] -= 1
        root.left = self._helper(inorder, postorder, index, p_index, target)
        return root
