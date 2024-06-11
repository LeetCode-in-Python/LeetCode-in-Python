206\. Reverse Linked List

Easy

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**Input:** head = [1,2,3,4,5]

**Output:** [5,4,3,2,1] 

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

**Input:** head = [1,2]

**Output:** [2,1] 

**Example 3:**

**Input:** head = []

**Output:** [] 

**Constraints:**

*   The number of nodes in the list is the range `[0, 5000]`.
*   `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

To solve the Reverse Linked List problem, we can either use an iterative approach or a recursive approach. Here are the steps for both approaches:

### Iterative Approach:
1. **Initialize Pointers**: Initialize three pointers, `prev`, `curr`, and `next`.
2. **Iterate Through List**: Iterate through the list until `curr` is not `None`.
   - Update `next` to `curr.next`.
   - Reverse the `curr` node's pointer to point to `prev` instead of `next`.
   - Move `prev` to `curr` and `curr` to `next`.
3. **Return Head**: Return `prev` as the new head of the reversed list.

### Recursive Approach:
1. **Define Recursive Function**: Define a recursive function that takes a node as input.
2. **Base Case**: If the input node or its next node is `None`, return the node itself.
3. **Recursive Call**: Recursively call the function on the next node.
4. **Reverse Pointers**: Reverse the pointers of the current node and its next node.
5. **Return Head**: Return the new head of the reversed list.

Let's implement both approaches:

```python
class Solution:
    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        def reverse(node):
            if not node or not node.next:
                return node
            new_head = reverse(node.next)
            node.next.next = node
            node.next = None
            return new_head
        
        return reverse(head)
```

These solutions will efficiently reverse the linked list either iteratively or recursively, meeting the problem constraints. The time complexity for both approaches is O(n), where n is the number of nodes in the linked list.