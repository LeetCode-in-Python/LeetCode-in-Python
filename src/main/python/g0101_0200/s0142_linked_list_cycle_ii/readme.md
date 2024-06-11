142\. Linked List Cycle II

Medium

Given the `head` of a linked list, return _the node where the cycle begins. If there is no cycle, return_ `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Input:** head = [3,2,0,-4], pos = 1

**Output:** tail connects to node index 1

**Explanation:** There is a cycle in the linked list, where tail connects to the second node. 

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Input:** head = [1,2], pos = 0

**Output:** tail connects to node index 0

**Explanation:** There is a cycle in the linked list, where tail connects to the first node. 

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**Input:** head = [1], pos = -1

**Output:** no cycle

**Explanation:** There is no cycle in the linked list. 

**Constraints:**

*   The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>
*   `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

To solve the problem, we can use Floyd's Tortoise and Hare algorithm, also known as the Floyd's Cycle Detection algorithm. This algorithm involves two pointers, one moving at twice the speed of the other. If there's a cycle in the linked list, these two pointers will eventually meet. Once they meet, we reset one pointer to the head of the list and move both pointers at the same speed. The point where they meet again will be the start of the cycle.

Here's how we can implement this algorithm in Python using a `Solution` class:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Function to detect cycle and return the node where cycle starts
        
        # Step 1: Initialize slow and fast pointers
        slow = fast = head
        
        # Step 2: Find the meeting point of the two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # If there's no cycle, return None
        if not fast or not fast.next:
            return None
        
        # Step 3: Reset one pointer to the head and move both pointers at the same speed
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Step 4: Return the node where the two pointers meet again (start of cycle)
        return slow

# Example usage:
# Create linked list nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Connect nodes to form a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # This creates a cycle

# Create an instance of Solution class
solution = Solution()

# Call detectCycle method to find the start of the cycle
cycle_start = solution.detectCycle(node1)

if cycle_start:
    print("Tail connects to node index:", cycle_start.val)
else:
    print("No cycle")
```

This solution has a time complexity of O(n) and uses O(1) extra space.