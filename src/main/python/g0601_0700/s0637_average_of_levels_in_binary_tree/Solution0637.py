# #Easy #Depth_First_Search #Breadth_First_Search #Tree #Binary_Tree
# #Top_Interview_150_Binary_Tree_BFS #2025_09_20_Time_0_ms_(100.00%)_Space_20.04_MB_(13.04%)

from typing import List, Optional, Dict

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        ans = []
        while q:
            s = 0
            nq = []
            for u in q:
                s += u.val
                if u.left:
                    nq.append(u.left)
                if u.right:
                    nq.append(u.right)
            ans.append(s/len(q))
            q = nq
        return ans
