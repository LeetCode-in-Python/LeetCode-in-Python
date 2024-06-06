2\. Add Two Numbers

Medium

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

**Input:** l1 = [2,4,3], l2 = [5,6,4]

**Output:** [7,0,8]

**Explanation:** 342 + 465 = 807. 

**Example 2:**

**Input:** l1 = [0], l2 = [0]

**Output:** [0] 

**Example 3:**

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]

**Output:** [8,9,9,9,0,0,0,1] 

**Constraints:**

*   The number of nodes in each linked list is in the range `[1, 100]`.
*   `0 <= Node.val <= 9`
*   It is guaranteed that the list represents a number that does not have leading zeros.

Here are the steps to solve the "Add Two Numbers" problem:

### Approach:

1. **Initialize Pointers and Carry:**
   - Initialize three pointers, `p1` for the first linked list (`l1`), `p2` for the second linked list (`l2`), and `dummy_head` for the dummy node of the result linked list.
   - Initialize `carry` to 0.

2. **Traverse Both Linked Lists:**
   - Traverse both linked lists until both pointers (`p1` and `p2`) reach the end.

3. **Calculate Sum and Carry:**
   - At each step, calculate the sum of the current digits and the carry from the previous step.
   - Update `carry` for the next iteration.

4. **Create New Node:**
   - Create a new node with the value as the sum % 10 and add it to the result linked list.

5. **Move Pointers:**
   - Move both pointers (`p1` and `p2`) to the next nodes in their respective linked lists.

6. **Handle Remaining Digits:**
   - After both linked lists are traversed, check if there is any remaining carry.
   - If there is, create a new node with the value of the carry and add it to the result linked list.

7. **Return Result:**
   - Return the next node of `dummy_head` as the head of the result linked list.

### Python Code:

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        p1, p2, current = l1, l2, dummy_head
        carry = 0

        while p1 or p2:
            # Get values and handle None cases
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0

            # Calculate sum and carry
            _sum = x + y + carry
            carry = _sum // 10

            # Create new node with the sum % 10
            current.next = ListNode(_sum % 10)
            current = current.next

            # Move pointers to the next nodes
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        # Handle remaining carry
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next

# Example Usage:
solution = Solution()

# Example 1:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = solution.addTwoNumbers(l1, l2)
# Output: [7, 0, 8]

# Example 2:
l1 = ListNode(0)
l2 = ListNode(0)
result = solution.addTwoNumbers(l1, l2)
# Output: [0]

# Example 3:
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
result = solution.addTwoNumbers(l1, l2)
# Output: [8, 9, 9, 9, 0, 0, 0, 1]
```

This code defines a `ListNode` class for the singly-linked list and a `Solution` class with a method `addTwoNumbers` that takes two linked lists as input and returns the result as a linked list. The example usage demonstrates how to create instances of the `ListNode` class and call the `addTwoNumbers` method with different inputs.