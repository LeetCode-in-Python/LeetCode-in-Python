21\. Merge Two Sorted Lists

Easy

Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

**Input:** l1 = [1,2,4], l2 = [1,3,4]

**Output:** [1,1,2,3,4,4] 

**Example 2:**

**Input:** l1 = [], l2 = []

**Output:** [] 

**Example 3:**

**Input:** l1 = [], l2 = [0]

**Output:** [0] 

**Constraints:**

*   The number of nodes in both lists is in the range `[0, 50]`.
*   `-100 <= Node.val <= 100`
*   Both `l1` and `l2` are sorted in **non-decreasing** order.

Here are the steps to solve the "Merge Two Sorted Lists" problem:

### Approach:

1. **Initialize Dummy Node:**
   - Initialize a dummy node to simplify the code. The dummy node's next pointer will point to the head of the merged list.

2. **Initialize Pointers:**
   - Initialize pointers `curr` and `prev` initially pointing to the dummy node.

3. **Merge Lists:**
   - Iterate until either `l1` or `l2` becomes `None`. In each iteration:
     - Compare the values of the current nodes in `l1` and `l2`.
     - Connect the smaller node to the merged list.
     - Move the corresponding pointer (`l1` or `l2`) to its next node.
     - Move the `curr` pointer to the newly added node.

4. **Handle Remaining Nodes:**
   - After the loop, if there are remaining nodes in either `l1` or `l2`, connect them to the merged list.

5. **Return Merged List:**
   - Return the next of the dummy node, which is the head of the merged list.

### Python Code:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize dummy node
        dummy = ListNode()
        # Initialize pointers
        curr = dummy
        # Merge lists
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        # Handle remaining nodes
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        # Return merged list
        return dummy.next

# Example Usage:
solution = Solution()

# Example 1:
l1_1 = ListNode(1, ListNode(2, ListNode(4)))
l2_1 = ListNode(1, ListNode(3, ListNode(4)))
result1 = solution.mergeTwoLists(l1_1, l2_1)  # Output: ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

# Example 2:
l1_2 = None
l2_2 = None
result2 = solution.mergeTwoLists(l1_2, l2_2)  # Output: None (empty list)

# Example 3:
l1_3 = None
l2_3 = ListNode(0)
result3 = solution.mergeTwoLists(l1_3, l2_3)  # Output: ListNode(0)
```

This code defines a `ListNode` class representing a node in the linked list and a `Solution` class with a method `mergeTwoLists` that takes two sorted linked lists (`l1` and `l2`) as input and returns a new sorted linked list obtained by merging the nodes of `l1` and `l2`. The example usage demonstrates how to create instances of the `ListNode` class and call the `mergeTwoLists` method with different inputs.