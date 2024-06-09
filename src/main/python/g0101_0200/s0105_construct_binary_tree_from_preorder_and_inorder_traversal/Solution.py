# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Tree #Binary_Tree
# #Divide_and_Conquer #Data_Structure_II_Day_15_Tree #Big_O_Time_O(N)_Space_O(N)
# #2024_06_09_Time_45_ms_(96.51%)_Space_18.1_MB_(90.27%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.j = 0
        self.map = {}

    def get(self, key: int) -> int:
        return self.map[key]

    def answer(self, preorder: List[int], inorder: List[int], start: int, end: int) -> TreeNode:
        if start > end or self.j > len(preorder):
            return None
        value = preorder[self.j]
        self.j += 1
        index = self.get(value)
        node = TreeNode(value)
        node.left = self.answer(preorder, inorder, start, index - 1)
        node.right = self.answer(preorder, inorder, index + 1, end)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.j = 0
        for i in range(len(preorder)):
            self.map[inorder[i]] = i
        return self.answer(preorder, inorder, 0, len(preorder) - 1)
