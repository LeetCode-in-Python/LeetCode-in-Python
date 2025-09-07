# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Breadth_First_Search #Tree
# #Binary_Tree #Data_Structure_I_Day_11_Tree #Level_1_Day_6_Tree #Udemy_Tree_Stack_Queue
# #Top_Interview_150_Binary_Tree_BFS #Big_O_Time_O(N)_Space_O(N)
# #2025_07_24_Time_0_ms_(100.00%)_Space_18.34_MB_(87.01%)

from typing import Optional, List
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

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        level = []
        while queue:
            node = queue.popleft()
            if node is not None:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                result.append(level)
                level = []
                if queue:
                    queue.append(None)
        
        return result
