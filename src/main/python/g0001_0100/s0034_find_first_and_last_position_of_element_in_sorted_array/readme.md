34\. Find First and Last Position of Element in Sorted Array

Medium

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = [5,7,7,8,8,10], target = 8

**Output:** [3,4] 

**Example 2:**

**Input:** nums = [5,7,7,8,8,10], target = 6

**Output:** [-1,-1] 

**Example 3:**

**Input:** nums = [], target = 0

**Output:** [-1,-1] 

**Constraints:**

*   <code>0 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>
*   `nums` is a non-decreasing array.
*   <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code>

To solve this problem efficiently with a runtime complexity of O(log n), we can use binary search to find the starting and ending positions of the target value in the sorted array. Here are the steps:

### Approach:

1. **Binary Search for Starting Position:**
   - Use binary search to find the starting position of the target value.
   - When the target value is found, continue searching towards the left to find the leftmost occurrence.
   - Update the left boundary to narrow down the search space.

2. **Binary Search for Ending Position:**
   - Use binary search to find the ending position of the target value.
   - When the target value is found, continue searching towards the right to find the rightmost occurrence.
   - Update the right boundary to narrow down the search space.

3. **Handle Missing Target:**
   - If the target value is not found, return [-1, -1].

### Python Code:

```python
class Solution:
    def searchRange(self, nums, target):
        def search_boundary(nums, target, is_left):
            left, right = 0, len(nums) - 1
            boundary = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    boundary = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return boundary

        left_boundary = search_boundary(nums, target, is_left=True)
        right_boundary = search_boundary(nums, target, is_left=False)

        return [left_boundary, right_boundary]

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(solution.searchRange(nums1, target1))  # Output: [3, 4]

# Example 2:
nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(solution.searchRange(nums2, target2))  # Output: [-1, -1]

# Example 3:
nums3 = []
target3 = 0
print(solution.searchRange(nums3, target3))  # Output: [-1, -1]
```

This code defines a `Solution` class with a `searchRange` method to find the starting and ending positions of the target value in the given array. The example usage demonstrates how to create an instance of the `Solution` class and call the `searchRange` method with different inputs.