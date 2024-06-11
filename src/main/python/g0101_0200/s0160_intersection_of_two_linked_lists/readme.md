160\. Intersection of Two Linked Lists

Easy

Given the heads of two singly linked-lists `headA` and `headB`, return _the node at which the two lists intersect_. If the two linked lists have no intersection at all, return `null`.

For example, the following two linked lists begin to intersect at node `c1`:

![](https://assets.leetcode.com/uploads/2021/03/05/160_statement.png)

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

**Note** that the linked lists must **retain their original structure** after the function returns.

**Custom Judge:**

The inputs to the **judge** are given as follows (your program is **not** given these inputs):

*   `intersectVal` - The value of the node where the intersection occurs. This is `0` if there is no intersected node.
*   `listA` - The first linked list.
*   `listB` - The second linked list.
*   `skipA` - The number of nodes to skip ahead in `listA` (starting from the head) to get to the intersected node.
*   `skipB` - The number of nodes to skip ahead in `listB` (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, `headA` and `headB` to your program. If you correctly return the intersected node, then your solution will be **accepted**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png)

**Input:** intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3

**Output:** Intersected at '8'

**Explanation:** The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B. 

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png)

**Input:** intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1

**Output:** Intersected at '2'

**Explanation:** The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B. 

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png)

**Input:** intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2

**Output:** No intersection

**Explanation:** From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values. Explanation: The two lists do not intersect, so return null. 

**Constraints:**

*   The number of nodes of `listA` is in the `m`.
*   The number of nodes of `listB` is in the `n`.
*   <code>0 <= m, n <= 3 * 10<sup>4</sup></code>
*   <code>1 <= Node.val <= 10<sup>5</sup></code>
*   `0 <= skipA <= m`
*   `0 <= skipB <= n`
*   `intersectVal` is `0` if `listA` and `listB` do not intersect.
*   `intersectVal == listA[skipA] == listB[skipB]` if `listA` and `listB` intersect.

**Follow up:** Could you write a solution that runs in `O(n)` time and use only `O(1)` memory?

To solve the problem of finding the intersection of two linked lists, we can use an efficient approach that leverages the properties of linked lists and ensures that the solution runs in O(n) time and uses O(1) extra space.

### Steps:

1. **Calculate the Lengths**:
   - Traverse both linked lists to calculate their lengths.

2. **Align the Starting Points**:
   - If one list is longer than the other, advance the pointer of the longer list by the difference in lengths. This way, both pointers are equidistant from the intersection point (if it exists).

3. **Find the Intersection**:
   - Traverse both lists simultaneously, comparing nodes to see if they are the same. The first common node is the intersection point.

### Implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        # Get the lengths of both linked lists
        lengthA = get_length(headA)
        lengthB = get_length(headB)

        # Align the starting points of both linked lists
        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1
        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1

        # Traverse both lists together to find the intersection
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
```

### Explanation:

1. **Calculate the Lengths**:
   - The `get_length` function calculates the length of a linked list by traversing it from the head to the end.
   - We calculate `lengthA` for `headA` and `lengthB` for `headB`.

2. **Align the Starting Points**:
   - If `lengthA` is greater than `lengthB`, we advance `headA` by `lengthA - lengthB` steps.
   - If `lengthB` is greater than `lengthA`, we advance `headB` by `lengthB - lengthA` steps.
   - This ensures that both pointers are the same distance away from the potential intersection point.

3. **Find the Intersection**:
   - We traverse both lists simultaneously, comparing the nodes. If `headA` is equal to `headB`, we've found the intersection point and return it.
   - If the traversal completes without finding an intersection, we return `None`.

This approach ensures that we only traverse each list a maximum of twice (once to calculate lengths and once to find the intersection), making the solution efficient with O(n) time complexity and O(1) space complexity.