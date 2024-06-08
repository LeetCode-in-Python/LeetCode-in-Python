33\. Search in Rotated Sorted Array

Medium

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of_ `target` _if it is in_ `nums`_, or_ `-1` _if it is not in_ `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = [4,5,6,7,0,1,2], target = 0

**Output:** 4 

**Example 2:**

**Input:** nums = [4,5,6,7,0,1,2], target = 3

**Output:** -1 

**Example 3:**

**Input:** nums = [1], target = 0

**Output:** -1 

**Constraints:**

*   `1 <= nums.length <= 5000`
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   All values of `nums` are **unique**.
*   `nums` is an ascending array that is possibly rotated.
*   <code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code>

To solve the "Search in Rotated Sorted Array" problem, you can use a modified binary search algorithm. Here are the steps:

### Approach:

1. **Find the Pivot:**
   - Use binary search to find the pivot index where the array is rotated.
   - The pivot is the index where `nums[pivot] > nums[pivot+1]`.

2. **Perform Binary Search:**
   - Compare the target with the first element of the array.
   - If the target is greater, perform a binary search in the second half.
   - If the target is smaller, perform a binary search in the first half.

3. **Binary Search:**
   - Use a standard binary search algorithm to find the target in the selected half of the array.
   - Update the mid index and adjust the search space accordingly.

4. **Handle Rotation:**
   - Adjust the mid index based on the pivot to consider the rotation.

5. **Handle Missing Elements:**
   - If the target is not found, return -1.

### Python Code:

```python
class Solution:
    def search(self, nums, target):
        # Function to find the index of the pivot
        def find_pivot(nums):
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] > nums[mid + 1]:
                    return mid + 1  # Found the pivot
                elif nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid

            return 0  # No rotation, array is not rotated

        # Function to perform binary search in the rotated array
        def binary_search(nums, target, left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        pivot = find_pivot(nums)

        # Check which half of the array to search
        if pivot == 0 or target < nums[0]:
            return binary_search(nums, target, pivot, len(nums) - 1)
        else:
            return binary_search(nums, target, 0, pivot - 1)

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(solution.search(nums1, target1))  # Output: 4

# Example 2:
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(solution.search(nums2, target2))  # Output: -1

# Example 3:
nums3 = [1]
target3 = 0
print(solution.search(nums3, target3))  # Output: -1
```

This code defines a `Solution` class with methods to find the pivot and perform binary search in the rotated array. The example usage demonstrates how to create an instance of the `Solution` class and call the `search` method with different inputs.