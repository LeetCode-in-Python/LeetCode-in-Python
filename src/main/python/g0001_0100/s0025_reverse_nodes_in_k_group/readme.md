25\. Reverse Nodes in k-Group

Hard

Given a linked list, reverse the nodes of a linked list _k_ at a time and return its modified list.

_k_ is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of _k_ then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

**Input:** head = [1,2,3,4,5], k = 2

**Output:** [2,1,4,3,5] 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

**Input:** head = [1,2,3,4,5], k = 3

**Output:** [3,2,1,4,5] 

**Example 3:**

**Input:** head = [1,2,3,4,5], k = 1

**Output:** [1,2,3,4,5] 

**Example 4:**

**Input:** head = [1], k = 1

**Output:** [1] 

**Constraints:**

*   The number of nodes in the list is in the range `sz`.
*   `1 <= sz <= 5000`
*   `0 <= Node.val <= 1000`
*   `1 <= k <= sz`

**Follow-up:** Can you solve the problem in O(1) extra memory space?

To solve the "Reverse Nodes in k-Group" problem, you can use the following approach:

### Approach:

1. **Check if Reversal is Possible:**
   - Before reversing, check if there are at least `k` nodes remaining in the linked list.

2. **Reverse Nodes:**
   - Reverse the next `k` nodes of the linked list.

3. **Connect the Reversed Portion:**
   - Connect the reversed portion to the previous part of the linked list.

4. **Update Pointers:**
   - Move the pointers to their correct positions for the next iteration.

5. **Repeat:**
   - Repeat the process until there are fewer than `k` nodes left.

6. **Return Result:**
   - Return the modified head of the linked list.

### Python Code:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Function to reverse a linked list
        def reverseList(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Initialize pointers
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        # Find the length of the linked list
        length = 0
        while head:
            length += 1
            head = head.next

        # Reverse nodes in k-group
        while length >= k:
            end = curr
            for _ in range(k - 1):
                end = end.next

            # Reverse k nodes
            next_start = end.next
            reversed_start = reverseList(curr, next_start)

            # Connect reversed portion to the previous part
            prev.next = reversed_start
            curr.next = next_start

            # Move pointers for the next iteration
            prev, curr = curr, next_start
            length -= k

        # Return the modified head
        return dummy.next

# Example Usage:
solution = Solution()

# Example 1:
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = solution.reverseKGroup(head1, 2)  # Output: ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5))))))

# Example 2:
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result2 = solution.reverseKGroup(head2, 3)  # Output: ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5))))))

# Example 3:
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result3 = solution.reverseKGroup(head3, 1)  # Output: ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Example 4:
head4 = ListNode(1)
result4 = solution.reverseKGroup(head4, 1)  # Output: ListNode(1)
```

This code defines a `Solution` class with a method `reverseKGroup` that takes a linked list and an integer `k` as input and reverses every `k` nodes in the linked list. The example usage demonstrates how to create an instance of the `Solution` class and call the `reverseKGroup` method with different inputs.