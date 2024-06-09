104\. Maximum Depth of Binary Tree

Easy

Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

**Input:** root = [3,9,20,null,null,15,7]

**Output:** 3 

**Example 2:**

**Input:** root = [1,null,2]

**Output:** 2 

**Example 3:**

**Input:** root = []

**Output:** 0 

**Example 4:**

**Input:** root = [0]

**Output:** 1 

**Constraints:**

*   The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
*   `-100 <= Node.val <= 100`

To solve the "Maximum Depth of Binary Tree" problem in Python with a `Solution` class, we'll perform a depth-first search (DFS) traversal of the binary tree. Below are the steps:

1. **Create a `Solution` class**: Define a class named `Solution` to encapsulate our solution methods.

2. **Create a `maxDepth` method**: This method takes the root node of the binary tree as input and returns its maximum depth.

3. **Check for null root**: Check if the root is null. If it is, return 0 as the depth.

4. **Perform DFS traversal**: Recursively compute the depth of the left and right subtrees. The maximum depth of the binary tree is the maximum depth of its left and right subtrees, plus 1 for the current node.

5. **Return the result**: After the DFS traversal is complete, return the maximum depth of the binary tree.

Here's the Python implementation:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right),
        )
```

This implementation follows the steps outlined above and efficiently computes the maximum depth of the binary tree in Python using DFS traversal.