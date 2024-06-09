98\. Validate Binary Search Tree

Medium

Given the `root` of a binary tree, _determine if it is a valid binary search tree (BST)_.

A **valid BST** is defined as follows:

*   The left subtree of a node contains only nodes with keys **less than** the node's key.
*   The right subtree of a node contains only nodes with keys **greater than** the node's key.
*   Both the left and right subtrees must also be binary search trees.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

**Input:** root = [2,1,3]

**Output:** true 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

**Input:** root = [5,1,4,null,null,3,6]

**Output:** false

**Explanation:** The root node's value is 5 but its right child's value is 4. 

**Constraints:**

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1</code>

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `isValidBST` that takes `root` as an input parameter.
3. Implement an algorithm to determine if the given binary tree is a valid binary search tree (BST).
4. Use the properties of a BST to perform an inorder traversal of the tree.
5. During the inorder traversal, keep track of the previous node's value to compare it with the current node's value.
6. If the current node's value is less than or equal to the previous node's value, return False.
7. After completing the traversal, return True, indicating that the tree is a valid BST.

Here's the implementation:

```python
class Solution:
    def isValidBST(self, root):
        def inorder_traversal(node, prev):
            if not node:
                return True
            
            if not inorder_traversal(node.left, prev):
                return False
            
            if prev[0] is not None and node.val <= prev[0]:
                return False
            
            prev[0] = node.val
            
            return inorder_traversal(node.right, prev)
        
        prev = [None]
        return inorder_traversal(root, prev)

# Example usage:
solution = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(solution.isValidBST(root1))  # Output: True

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(solution.isValidBST(root2))  # Output: False
```

This solution performs an inorder traversal of the binary tree and checks if the traversal sequence is sorted, indicating a valid BST. It has a time complexity of O(n), where n is the number of nodes in the tree, as it traverses each node exactly once.