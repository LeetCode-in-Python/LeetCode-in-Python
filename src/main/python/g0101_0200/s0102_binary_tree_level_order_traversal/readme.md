102\. Binary Tree Level Order Traversal

Medium

Given the `root` of a binary tree, return _the level order traversal of its nodes' values_. (i.e., from left to right, level by level).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**Input:** root = [3,9,20,null,null,15,7]

**Output:** [[3],[9,20],[15,7]] 

**Example 2:**

**Input:** root = [1]

**Output:** [[1]] 

**Example 3:**

**Input:** root = []

**Output:** [] 

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 2000]`.
*   `-1000 <= Node.val <= 1000`

To solve the "Binary Tree Level Order Traversal" problem in Python with a `Solution` class, we'll perform a breadth-first search (BFS) traversal of the binary tree. Below are the steps:

1. **Create a `Solution` class**: Define a class named `Solution` to encapsulate our solution methods.

2. **Create a `levelOrder` method**: This method takes the root node of the binary tree as input and returns the level order traversal of its nodes' values.

3. **Initialize a queue**: Create a queue to store the nodes during BFS traversal.

4. **Check for null root**: Check if the root is null. If it is, return an empty list.

5. **Perform BFS traversal**: Enqueue the root node into the queue. While the queue is not empty:
   - Dequeue the front node from the queue.
   - Add the value of the dequeued node to the current level list.
   - Enqueue the left and right children of the dequeued node if they exist.
   - Move to the next level when all nodes in the current level are processed.

6. **Return the result**: After the BFS traversal is complete, return the list containing the level order traversal of the binary tree.

Here's the Python implementation:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        level = []
        while queue:
            node = queue.popleft()
            if node is not None:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                result.append(level)
                level = []
                if queue:
                    queue.append(None)
        
        return result
```

This implementation follows the steps outlined above and efficiently computes the level order traversal of the binary tree in Python using BFS.