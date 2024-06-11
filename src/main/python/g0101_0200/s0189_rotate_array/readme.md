189\. Rotate Array

Medium

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

**Input:** nums = [1,2,3,4,5,6,7], k = 3

**Output:** [5,6,7,1,2,3,4]

**Explanation:**

    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4] 

**Example 2:**

**Input:** nums = [-1,-100,3,99], k = 2

**Output:** [3,99,-1,-100]

**Explanation:**

    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100] 

**Constraints:**

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>
*   <code>0 <= k <= 10<sup>5</sup></code>

**Follow up:**

*   Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
*   Could you do it in-place with `O(1)` extra space?

To solve the problem and rotate the array to the right by `k` steps, we can use multiple approaches. One efficient way is to use array reversal. This approach requires O(1) extra space.

### Steps:

1. **Reverse the Entire Array**:
   - Reverse the entire array.

2. **Reverse the First `k` Elements**:
   - Reverse the first `k` elements of the array.

3. **Reverse the Remaining Elements**:
   - Reverse the remaining elements of the array after the first `k` elements.

### Implementation:

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n

        # Reverse the entire array
        reverse(nums, 0, n - 1)

        # Reverse the first k elements
        reverse(nums, 0, k - 1)

        # Reverse the remaining elements
        reverse(nums, k, n - 1)
```

### Explanation:

1. **Reverse the Entire Array**:
   - The `reverse` function is defined to reverse a portion of the array between indices `start` and `end`.
   - We call `reverse(nums, 0, n - 1)` to reverse the entire array.

2. **Reverse the First `k` Elements**:
   - We calculate `k` as `k %= n` to handle cases where `k` is greater than the length of the array.
   - We call `reverse(nums, 0, k - 1)` to reverse the first `k` elements of the array.

3. **Reverse the Remaining Elements**:
   - We call `reverse(nums, k, n - 1)` to reverse the remaining elements of the array after the first `k` elements.

By following these steps, the array will be rotated to the right by `k` steps. This approach ensures that the rotation is done in-place with O(1) extra space and is efficient with a time complexity of O(n).