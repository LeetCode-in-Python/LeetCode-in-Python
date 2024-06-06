23\. Merge k Sorted Lists

Hard

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

**Example 1:**

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]

**Output:** [1,1,2,3,4,4,5,6]

**Explanation:** The linked-lists are: [ 1->4->5, 1->3->4, 2->6 ] merging them into one sorted list: 1->1->2->3->4->4->5->6 

**Example 2:**

**Input:** lists = []

**Output:** [] 

**Example 3:**

**Input:** lists = [[]]

**Output:** [] 

**Constraints:**

*   `k == lists.length`
*   `0 <= k <= 10^4`
*   `0 <= lists[i].length <= 500`
*   `-10^4 <= lists[i][j] <= 10^4`
*   `lists[i]` is sorted in **ascending order**.
*   The sum of `lists[i].length` won't exceed `10^4`.

To solve the "Merge k Sorted Lists" problem, you can follow these steps:

### Approach:

1. **Initialize a Priority Queue (Min-Heap):**
   - Initialize a priority queue (min-heap) to store nodes from all linked lists based on their values.

2. **Populate Priority Queue:**
   - Iterate through each linked list and insert the first node (if not None) from each list into the priority queue.

3. **Merge Lists using Priority Queue:**
   - While the priority queue is not empty:
     - Pop the smallest node from the priority queue.
     - Append the node's value to the result list.
     - If the node has a next element, insert the next node into the priority queue.

4. **Return Result List:**
   - Return the merged result list.

### Python Code:

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Initialize a priority queue
        heap = []
        
        # Populate priority queue with the first node from each list
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        # Initialize result dummy node and pointer
        result_dummy = ListNode()
        current = result_dummy

        # Merge lists using priority queue
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # Return merged result
        return result_dummy.next

# Example Usage:
solution = Solution()

# Example 1:
lists1 = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
result1 = solution.mergeKLists(lists1)  # Output: ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))

# Example 2:
lists2 = []
result2 = solution.mergeKLists(lists2)  # Output: None

# Example 3:
lists3 = [[]]
result3 = solution.mergeKLists(lists3)  # Output: None
```

This code defines a `Solution` class with a method `mergeKLists` that takes a list of linked lists as input and returns a merged sorted linked list. The example usage demonstrates how to create an instance of the `Solution` class and call the `mergeKLists` method with different inputs.