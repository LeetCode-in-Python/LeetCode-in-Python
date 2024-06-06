19\. Remove Nth Node From End of List

Medium

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

**Input:** head = [1,2,3,4,5], n = 2

**Output:** [1,2,3,5] 

**Example 2:**

**Input:** head = [1], n = 1

**Output:** [] 

**Example 3:**

**Input:** head = [1,2], n = 1

**Output:** [1] 

**Constraints:**

*   The number of nodes in the list is `sz`.
*   `1 <= sz <= 30`
*   `0 <= Node.val <= 100`
*   `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

Here are the steps to solve the "Remove Nth Node From End of List" problem:

### Approach:

1. **Initialize Pointers:**
   - Initialize two pointers, `fast` and `slow`, both initially pointing to the head of the linked list.

2. **Move Fast Pointer:**
   - Move the `fast` pointer `n` nodes ahead.

3. **Handle Edge Case:**
   - If the `fast` pointer becomes `None` after moving `n` nodes, it means the node to be removed is the head of the list. In this case, return `head.next`.

4. **Move Both Pointers Until Fast Reaches End:**
   - Move both `fast` and `slow` pointers one node at a time until the `fast` pointer reaches the end of the list.

5. **Remove Nth Node:**
   - Update the next pointer of the `slow` pointer to skip the node to be removed.

6. **Return Updated Head:**
   - Return the head of the modified linked list.

### Python Code:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Initialize pointers
        fast = slow = head

        # Move fast pointer n nodes ahead
        for _ in range(n):
            fast = fast.next

        # Handle case where the node to be removed is the head
        if not fast:
            return head.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove nth node
        slow.next = slow.next.next

        # Return updated head
        return head

# Example Usage:
solution = Solution()

# Example 1:
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n1 = 2
result1 = solution.removeNthFromEnd(head1, n1)  # Output: ListNode(1, ListNode(2, ListNode(3, ListNode(5))))

# Example 2:
head2 = ListNode(1)
n2 = 1
result2 = solution.removeNthFromEnd(head2, n2)  # Output: None (empty list)

# Example 3:
head3 = ListNode(1, ListNode(2))
n3 = 1
result3 = solution.removeNthFromEnd(head3, n3)  # Output: ListNode(1)
```

This code defines a `ListNode` class representing a node in the linked list and a `Solution` class with a method `removeNthFromEnd` that takes the head of the linked list and an integer `n` as input, removes the `nth` node from the end of the list, and returns the head of the modified list. The example usage demonstrates how to create instances of the `ListNode` class and call the `removeNthFromEnd` method with different inputs.