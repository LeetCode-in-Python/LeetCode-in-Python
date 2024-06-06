24\. Swap Nodes in Pairs

Medium

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

**Input:** head = [1,2,3,4]

**Output:** [2,1,4,3] 

**Example 2:**

**Input:** head = []

**Output:** [] 

**Example 3:**

**Input:** head = [1]

**Output:** [1] 

**Constraints:**

*   The number of nodes in the list is in the range `[0, 100]`.
*   `0 <= Node.val <= 100`

To solve the "Swap Nodes in Pairs" problem, you can follow these steps:

### Approach:

1. **Initialize a Dummy Node:**
   - Create a dummy node to simplify handling edge cases and to serve as the new head of the modified linked list.

2. **Initialize Pointers:**
   - Initialize three pointers: `prev`, `current`, and `next`.

3. **Iterate through Pairs:**
   - Use a loop to iterate through the linked list in pairs.
   - Inside the loop:
      - Update `prev.next` to point to the second node in the pair (`next`).
      - Update `current.next` to point to the node after the pair (`next.next`).
      - Update `next.next` to point to the first node in the pair (`current`).
      - Move `prev`, `current`, and `next` pointers to their next positions for the next pair.

4. **Return Modified Head:**
   - Return the `dummy.next` as the new head of the modified linked list.

### Python Code:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # Initialize a dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Iterate through pairs
        while head and head.next:
            # Initialize pointers
            current = head
            next_node = head.next

            # Swap pairs
            prev.next = next_node
            current.next = next_node.next
            next_node.next = current

            # Move pointers for the next pair
            prev = current
            head = current.next

        # Return modified head
        return dummy.next

# Example Usage:
solution = Solution()

# Example 1:
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result1 = solution.swapPairs(head1)  # Output: ListNode(2, ListNode(1, ListNode(4, ListNode(3))))

# Example 2:
head2 = None
result2 = solution.swapPairs(head2)  # Output: None

# Example 3:
head3 = ListNode(1)
result3 = solution.swapPairs(head3)  # Output: ListNode(1)
```

This code defines a `Solution` class with a method `swapPairs` that takes a linked list as input and swaps every two adjacent nodes. The example usage demonstrates how to create an instance of the `Solution` class and call the `swapPairs` method with different inputs.