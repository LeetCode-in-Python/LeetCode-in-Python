148\. Sort List

Medium

Given the `head` of a linked list, return _the list after sorting it in **ascending order**_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)

**Input:** head = [4,2,1,3]

**Output:** [1,2,3,4] 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)

**Input:** head = [-1,5,3,4,0]

**Output:** [-1,0,3,4,5] 

**Example 3:**

**Input:** head = []

**Output:** [] 

**Constraints:**

*   The number of nodes in the list is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?

To solve the problem of sorting a linked list, you can use the merge sort algorithm, which is suitable for linked lists because it provides an O(n log n) time complexity. This approach can be implemented recursively and achieves the required efficiency.

Here are the detailed steps and the corresponding implementation using the `Solution` class:

### Steps:

1. **Base Case**:
   - If the linked list is empty or has only one node, it is already sorted. Return the head.

2. **Split the List**:
   - Use the fast and slow pointer technique to find the middle of the linked list. This will help to split the linked list into two halves.
   - `slow` moves one step at a time, while `fast` moves two steps at a time.
   - When `fast` reaches the end, `slow` will be at the middle point of the list.

3. **Sort Each Half**:
   - Recursively sort the left half and the right half of the list.

4. **Merge the Sorted Halves**:
   - Merge the two sorted halves into a single sorted list.

### Implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # Step 2: Split the list into two halves
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None
        
        # Step 3: Sort each half
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Step 4: Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
```

### Explanation:

1. **Base Case**:
   - The function `sortList` checks if the list is empty or has a single node, in which case it returns the head as it is already sorted.

2. **Split the List**:
   - The `getMid` function finds the middle of the list using the fast and slow pointer technique.
   - The list is then split into two halves: `left` starting from the head to the middle, and `right` starting from the node after the middle.

3. **Sort Each Half**:
   - The `sortList` function is called recursively on both halves to sort them.

4. **Merge the Sorted Halves**:
   - The `merge` function merges the two sorted halves into a single sorted linked list.
   - A dummy node is used to simplify the merging process, and a `tail` pointer is used to build the new sorted list.

This approach ensures that the linked list is sorted in O(n log n) time complexity, which is optimal for this problem. The space complexity is O(log n) due to the recursion stack.