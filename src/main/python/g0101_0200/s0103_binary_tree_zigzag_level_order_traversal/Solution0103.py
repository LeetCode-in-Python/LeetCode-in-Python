# #Medium #Top_Interview_Questions #Breadth_First_Search #Tree #Binary_Tree
# #Data_Structure_II_Day_15_Tree #Udemy_Tree_Stack_Queue #Top_Interview_150_Binary_Tree_BFS
# #2025_09_14_Time_0_ms_(100.00%)_Space_18.25_MB_(8.14%)

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = deque()
        q.append(root)
        q.append(None)
        zig = True
        level = deque()
        while q:
            node = q.popleft()
            while q and node is not None:
                if zig:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                node = q.popleft()
            result.append(list(level))
            zig = not zig
            level = deque()
            if q:
                q.append(None)
        return result
