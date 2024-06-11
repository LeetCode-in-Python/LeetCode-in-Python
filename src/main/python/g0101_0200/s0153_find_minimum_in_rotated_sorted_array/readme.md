153\. Find Minimum in Rotated Sorted Array

Medium

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

*   `[4,5,6,7,0,1,2]` if it was rotated `4` times.
*   `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return _the minimum element of this array_.

You must write an algorithm that runs in `O(log n) time.`

**Example 1:**

**Input:** nums = [3,4,5,1,2]

**Output:** 1

**Explanation:** The original array was [1,2,3,4,5] rotated 3 times. 

**Example 2:**

**Input:** nums = [4,5,6,7,0,1,2]

**Output:** 0

**Explanation:** The original array was [0,1,2,4,5,6,7] and it was rotated 4 times. 

**Example 3:**

**Input:** nums = [11,13,15,17]

**Output:** 11

**Explanation:** The original array was [11,13,15,17] and it was rotated 4 times. 

**Constraints:**

*   `n == nums.length`
*   `1 <= n <= 5000`
*   `-5000 <= nums[i] <= 5000`
*   All the integers of `nums` are **unique**.
*   `nums` is sorted and rotated between `1` and `n` times.

To solve the problem, we can use a binary search approach. This method leverages the properties of the rotated array and achieves the required O(log n) time complexity.

### Steps:

1. **Initialization**:
   - Define two pointers, `left` and `right`, initialized to the start and end of the array, respectively.

2. **Binary Search**:
   - While `left` is less than `right`, perform the following steps:
     - Calculate the mid-point `mid` using integer division.
     - Determine if the middle element is greater than the rightmost element:
       - If `nums[mid]` is greater than `nums[right]`, it means the minimum element is in the right half of the array. Move the `left` pointer to `mid + 1`.
       - Otherwise, the minimum element is in the left half or could be the `mid` itself. Move the `right` pointer to `mid`.

3. **Return Result**:
   - After the loop terminates, the `left` pointer will point to the minimum element in the array.

### Implementation:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
```

### Explanation:

1. **Initialization**:
   - `left` starts at 0 and `right` starts at the last index of the array.

2. **Binary Search**:
   - The `while` loop runs as long as `left` is less than `right`.
   - `mid` is calculated as the average of `left` and `right`.
   - If the middle element `nums[mid]` is greater than `nums[right]`, it means the minimum value is in the right part of the array. We discard the left half by setting `left` to `mid + 1`.
   - If `nums[mid]` is less than or equal to `nums[right]`, it means the minimum value is in the left part, including `mid`. We set `right` to `mid`.

3. **Return Result**:
   - When the loop terminates, `left` will be at the index of the minimum element, so we return `nums[left]`.

This approach efficiently narrows down the search space by half in each iteration, ensuring a logarithmic time complexity.