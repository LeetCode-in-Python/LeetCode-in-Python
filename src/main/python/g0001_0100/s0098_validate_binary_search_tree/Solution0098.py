# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Depth_First_Search #Tree #Binary_Tree
# #Binary_Search_Tree #Data_Structure_I_Day_14_Tree #Level_1_Day_8_Binary_Search_Tree
# #Udemy_Tree_Stack_Queue #Top_Interview_150_Binary_Search_Tree #Big_O_Time_O(N)_Space_O(log(N))
# #2025_07_24_Time_0_ms_(100.00%)_Space_19.66_MB_(89.79%)

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.isValidBSTHelper(root,float('-inf'),float('+inf'))
        return ans

    def isValidBSTHelper(self,root,mini,maxi):
        if root==None:
            return True
        
        if root.val<mini or root.val>maxi:
            return False
        
        left = self.isValidBSTHelper(root.left,mini,root.val-1)
        right = self.isValidBSTHelper(root.right,root.val+1,maxi)

        if left==False or right==False:
            return False
        return True
