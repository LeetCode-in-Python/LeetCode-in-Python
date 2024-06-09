138\. Copy List with Random Pointer

Medium

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return _the head of the copied linked list_.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

*   `val`: an integer representing `Node.val`
*   `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

**Input:** head = [[7,null],[13,0],[11,4],[10,2],[1,0]]

**Output:** [[7,null],[13,0],[11,4],[10,2],[1,0]] 

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

**Input:** head = [[1,1],[2,1]]

**Output:** [[1,1],[2,1]] 

**Example 3:**

**![](https://assets.leetcode.com/uploads/2019/12/18/e3.png)**

**Input:** head = [[3,null],[3,0],[3,null]]

**Output:** [[3,null],[3,0],[3,null]] 

**Example 4:**

**Input:** head = []

**Output:** []

**Explanation:** The given linked list is empty (null pointer), so return null. 

**Constraints:**

*   `0 <= n <= 1000`
*   `-10000 <= Node.val <= 10000`
*   `Node.random` is `null` or is pointing to some node in the linked list.

To solve this problem with the `Solution` class, we can use a hashmap to keep track of the mapping between original nodes and their corresponding copied nodes. Here are the steps:

1. Define the `Solution` class with a method `copyRandomList` that takes the head of the original linked list as input and returns the head of the copied linked list.
2. Within the `copyRandomList` method, if the input `head` is `None`, return `None` as the copied list is empty.
3. Initialize an empty hashmap to store the mapping between original nodes and copied nodes.
4. Iterate through the original linked list and create a copied node for each original node. Set the value of the copied node to be the same as the original node and set both `next` and `random` pointers of the copied node to `None`.
5. Store the mapping between original nodes and copied nodes in the hashmap.
6. Iterate through the original linked list again and update the `next` and `random` pointers of copied nodes according to the mapping stored in the hashmap.
7. Finally, return the head of the copied linked list.

Here's how the `Solution` class would look like in Python:

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        mapping = {}
        
        # Create copies of nodes without pointers
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        # Assign pointers for each copied node
        current = head
        while current:
            mapping[current].next = mapping.get(current.next)
            mapping[current].random = mapping.get(current.random)
            current = current.next
        
        return mapping[head]
```

Make sure to define the `Node` class before using it in the `copyRandomList` method. This solution constructs a deep copy of the original linked list while maintaining the relationships between nodes as specified.