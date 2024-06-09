94\. Binary Tree Inorder Traversal

Easy

Given the `root` of a binary tree, return _the inorder traversal of its nodes' values_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

**Input:** root = [1,null,2,3]

**Output:** [1,3,2] 

**Example 2:**

**Input:** root = []

**Output:** [] 

**Example 3:**

**Input:** root = [1]

**Output:** [1] 

**Example 4:**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)

**Input:** root = [1,2]

**Output:** [2,1] 

**Example 5:**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

**Input:** root = [1,null,2]

**Output:** [1,2] 

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 100]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `inorderTraversal` that takes `root` as an input parameter.
3. Implement an algorithm to perform an inorder traversal of the binary tree iteratively.
4. Use a stack-based approach to simulate the recursion of inorder traversal.
5. Initialize an empty list `result` to store the inorder traversal sequence.
6. Initialize a stack to store nodes during traversal.
7. Start with the root node. While the current node is not None or the stack is not empty:
    - While the current node is not None, push the current node onto the stack and move to its left child.
    - Once the current node becomes None, pop the top node from the stack, add its value to the `result`, and move to its right child.
8. Return the `result` list containing the inorder traversal sequence.

Here's the implementation:

```python
class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result
```

This solution performs an inorder traversal of the binary tree iteratively using a stack-based approach. It traverses each node exactly once, resulting in a time complexity of O(n), where n is the number of nodes in the tree.