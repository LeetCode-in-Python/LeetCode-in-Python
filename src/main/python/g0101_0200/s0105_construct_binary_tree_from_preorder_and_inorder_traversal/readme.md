105\. Construct Binary Tree from Preorder and Inorder Traversal

Medium

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return _the binary tree_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

**Input:** preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

**Output:** [3,9,20,null,null,15,7] 

**Example 2:**

**Input:** preorder = [-1], inorder = [-1]

**Output:** [-1] 

**Constraints:**

*   `1 <= preorder.length <= 3000`
*   `inorder.length == preorder.length`
*   `-3000 <= preorder[i], inorder[i] <= 3000`
*   `preorder` and `inorder` consist of **unique** values.
*   Each value of `inorder` also appears in `preorder`.
*   `preorder` is **guaranteed** to be the preorder traversal of the tree.
*   `inorder` is **guaranteed** to be the inorder traversal of the tree.

To solve the "Construct Binary Tree from Preorder and Inorder Traversal" problem in Python with a `Solution` class, we'll use a recursive approach. Below are the steps:

1. **Create a `Solution` class**: Define a class named `Solution` to encapsulate our solution methods.

2. **Create a `buildTree` method**: This method takes two integer arrays, `preorder` and `inorder`, as input and returns the constructed binary tree.

3. **Check for empty arrays**: Check if either of the arrays `preorder` or `inorder` is empty. If so, return null, as there's no tree to construct.

4. **Define a helper method**: Define a recursive helper method `build` to construct the binary tree.
   - The method should take the indices representing the current subtree in both `preorder` and `inorder`.
   - The start and end indices in `preorder` represent the current subtree's preorder traversal.
   - The start and end indices in `inorder` represent the current subtree's inorder traversal.
   
5. **Base case**: If the start index of `preorder` is greater than the end index or if the start index of `inorder` is greater than the end index, return null.

6. **Find the root node**: The root node is the first element in the `preorder` array.

7. **Find the root's position in `inorder`**: Iterate through the `inorder` array to find the root's position.

8. **Recursively build left and right subtrees**: 
   - Recursively call the `build` method for the left subtree with updated indices.
   - Recursively call the `build` method for the right subtree with updated indices.
   
9. **Return the root node**: After constructing the left and right subtrees, return the root node.

Here's the Python implementation:

```python
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
```

This implementation follows the steps outlined above and efficiently constructs the binary tree from preorder and inorder traversals in Python.