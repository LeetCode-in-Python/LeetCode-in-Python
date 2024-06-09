101\. Symmetric Tree

Easy

Given the `root` of a binary tree, _check whether it is a mirror of itself_ (i.e., symmetric around its center).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

**Input:** root = [1,2,2,3,4,4,3]

**Output:** true 

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

**Input:** root = [1,2,2,null,3,null,3]

**Output:** false 

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 1000]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Could you solve it both recursively and iteratively?

To solve the "Symmetric Tree" problem in Python with the Solution class, follow these steps:

1. Define a method `isSymmetric` in the `Solution` class that takes the root of a binary tree as input and returns true if the tree is symmetric, and false otherwise.
2. Implement a recursive approach to check if the given binary tree is symmetric:
   - Define a helper method `isMirror` that takes two tree nodes as input parameters.
   - In the `isMirror` method, recursively compare the left and right subtrees of the given nodes.
   - At each step, check if the values of the corresponding nodes are equal and if the left subtree of one node is a mirror image of the right subtree of the other node.
   - If both conditions are satisfied for all corresponding nodes, return true; otherwise, return false.
3. Call the `isMirror` method with the root's left and right children to check if the entire tree is symmetric.

Here's the implementation of the `isSymmetric` method in Python:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, leftNode: TreeNode, rightNode: TreeNode) -> bool:
        if leftNode is None or rightNode is None:
            return leftNode is None and rightNode is None
        if leftNode.val != rightNode.val:
            return False
        return self.helper(leftNode.left, rightNode.right) and self.helper(leftNode.right, rightNode.left)
```

This implementation recursively checks whether the given binary tree is symmetric around its center in O(n) time complexity, where n is the number of nodes in the tree.