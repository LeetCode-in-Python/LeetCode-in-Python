141\. Linked List Cycle

Easy

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` _if there is a cycle in the linked list_. Otherwise, return `false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Input:** head = [3,2,0,-4], pos = 1

**Output:** true

**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed). 

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Input:** head = [1,2], pos = 0

**Output:** true

**Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node. 

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**Input:** head = [1], pos = -1

**Output:** false

**Explanation:** There is no cycle in the linked list. 

**Constraints:**

*   The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>
*   `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

To solve this problem with the `Solution` class, we can use Floyd's Tortoise and Hare algorithm, also known as the "slow and fast pointers" approach. Here are the steps:

1. Define the `Solution` class with a method `hasCycle` that takes the head of a linked list as input and returns a boolean indicating whether the linked list has a cycle.
2. Initialize two pointers, `slow` and `fast`, both pointing to the head of the linked list.
3. Iterate through the linked list using the slow and fast pointers.
4. Move the slow pointer one step at a time and the fast pointer two steps at a time.
5. If there is a cycle in the linked list, eventually the fast pointer will meet the slow pointer at some point.
6. If the fast pointer reaches the end of the list (`None`), it means there is no cycle, so return `False`.
7. If the fast and slow pointers meet, it means there is a cycle, so return `True`.

Here's how the `Solution` class would look like in Python:

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

# Example usage:
solution = Solution()
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next  # creates a cycle
print(solution.hasCycle(head1))  # Output: True

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2  # creates a cycle
print(solution.hasCycle(head2))  # Output: True

head3 = ListNode(1)
print(solution.hasCycle(head3))  # Output: False
```

This solution effectively uses Floyd's Tortoise and Hare algorithm to detect whether there is a cycle in the linked list, satisfying the constraints provided in the problem statement.