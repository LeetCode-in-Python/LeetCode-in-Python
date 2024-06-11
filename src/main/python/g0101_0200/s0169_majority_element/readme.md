169\. Majority Element

Easy

Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

**Input:** nums = [3,2,3]

**Output:** 3 

**Example 2:**

**Input:** nums = [2,2,1,1,1,2,2]

**Output:** 2 

**Constraints:**

*   `n == nums.length`
*   <code>1 <= n <= 5 * 10<sup>4</sup></code>
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

To solve the problem of finding the majority element in an array in linear time and with O(1) space, we can use the **Boyer-Moore Voting Algorithm**. This algorithm is efficient and meets the requirements perfectly.

### Steps:

1. **Initialization**:
   - Initialize two variables: `count` and `candidate`. The `count` is used to keep track of the number of occurrences of the current candidate for the majority element, and `candidate` stores the current candidate.

2. **First Pass - Find a Candidate**:
   - Traverse through the array and update the `candidate` and `count` based on the following rules:
     - If `count` is 0, set the current element as the `candidate` and set `count` to 1.
     - If the current element is the same as the `candidate`, increment the `count`.
     - If the current element is different from the `candidate`, decrement the `count`.

3. **Return the Candidate**:
   - The element stored in `candidate` after the first pass will be the majority element, as guaranteed by the problem statement.

### Implementation:

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
```

### Explanation:

1. **Initialization**:
   - `candidate` is initialized to `None` and `count` to `0`.

2. **First Pass - Find a Candidate**:
   - Loop through each element in the array `nums`:
     - If `count` is `0`, set the current element as the `candidate` and reset `count` to `1`.
     - If the current element is the same as the `candidate`, increment `count`.
     - If the current element is different from the `candidate`, decrement `count`.
   - This process ensures that the `candidate` will be the element that appears more than `⌊n / 2⌋` times by the end of the loop.

3. **Return the Candidate**:
   - Return the `candidate` as the majority element.

This approach is efficient with a time complexity of O(n) and a space complexity of O(1), meeting the problem constraints.