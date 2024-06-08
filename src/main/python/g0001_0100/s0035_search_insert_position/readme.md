35\. Search Insert Position

Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = [1,3,5,6], target = 5

**Output:** 2 

**Example 2:**

**Input:** nums = [1,3,5,6], target = 2

**Output:** 1 

**Example 3:**

**Input:** nums = [1,3,5,6], target = 7

**Output:** 4 

**Example 4:**

**Input:** nums = [1,3,5,6], target = 0

**Output:** 0 

**Example 5:**

**Input:** nums = [1], target = 0

**Output:** 0 

**Constraints:**

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   `nums` contains **distinct** values sorted in **ascending** order.
*   <code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code>

To solve this problem efficiently with a runtime complexity of O(log n), we can use binary search to find the insertion position of the target value in the sorted array. Here are the steps:

### Approach:

1. **Binary Search:**
   - Implement binary search to find the insertion position of the target value.
   - If the target value is found, return its index.
   - If the target value is not found, binary search will determine the index where the target would be inserted to maintain the sorted order.

### Python Code:

```python
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If the target is not found, return the insertion position (left).
        return left

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [1, 3, 5, 6]
target1 = 5
print(solution.searchInsert(nums1, target1))  # Output: 2

# Example 2:
nums2 = [1, 3, 5, 6]
target2 = 2
print(solution.searchInsert(nums2, target2))  # Output: 1

# Example 3:
nums3 = [1, 3, 5, 6]
target3 = 7
print(solution.searchInsert(nums3, target3))  # Output: 4

# Example 4:
nums4 = [1, 3, 5, 6]
target4 = 0
print(solution.searchInsert(nums4, target4))  # Output: 0

# Example 5:
nums5 = [1]
target5 = 0
print(solution.searchInsert(nums5, target5))  # Output: 0
```

This code defines a `Solution` class with a `searchInsert` method to find the insertion position of the target value in the given sorted array. The example usage demonstrates how to create an instance of the `Solution` class and call the `searchInsert` method with different inputs.