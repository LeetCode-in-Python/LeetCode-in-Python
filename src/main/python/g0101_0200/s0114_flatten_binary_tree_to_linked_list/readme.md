114\. Flatten Binary Tree to Linked List

Medium

Given the `root` of a binary tree, flatten the tree into a "linked list":

*   The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
*   The "linked list" should be in the same order as a [**pre-order** **traversal**](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR) of the binary tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)

**Input:** root = [1,2,5,3,4,null,6]

**Output:** [1,null,2,null,3,null,4,null,5,null,6] 

**Example 2:**

**Input:** root = []

**Output:** [] 

**Example 3:**

**Input:** root = [0]

**Output:** [0] 

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 2000]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?

To solve the "Flatten Binary Tree to Linked List" problem in Python with a `Solution` class, we'll use a recursive approach. Below are the steps:

1. **Create a `Solution` class**: Define a class named `Solution` to encapsulate our solution methods.

2. **Create a `flatten` method**: This method takes the root node of the binary tree as input and flattens the tree into a linked list using preorder traversal.

3. **Check for null root**: Check if the root is null. If so, there's no tree to flatten, so return.

4. **Recursively flatten the tree**: Define a recursive helper method `flattenTree` to perform the flattening.
   - The method should take the current node as input.
   - Perform a preorder traversal of the tree.
   - For each node, if it has a left child:
     - Find the rightmost node in the left subtree.
     - Attach the right subtree of the current node to the right of the rightmost node.
     - Move the left subtree to the right subtree position.
     - Set the left child of the current node to null.
   - Recursively call the method for the right child.

5. **Call the helper method**: Call the `flattenTree` method with the root node.

Here's the Python implementation:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.find_tail(root)

    def find_tail(self, root: TreeNode) -> TreeNode:
        left = root.left
        right = root.right
        # Find the tail of the left subtree, tail means the most left leaf
        if left:
            tail = self.find_tail(left)
            # Stitch the right subtree below the tail
            root.left = None
            root.right = left
            tail.right = right
        else:
            tail = root
        # Find tail of the right subtree
        if tail.right is None:
            return tail
        else:
            return self.find_tail(tail.right)   
```

This implementation follows the steps outlined above and efficiently flattens the binary tree into a linked list using preorder traversal in Python.