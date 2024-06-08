41\. First Missing Positive

Hard

Given an unsorted integer array `nums`, return the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses constant extra space.

**Example 1:**

**Input:** nums = [1,2,0]

**Output:** 3 

**Example 2:**

**Input:** nums = [3,4,-1,1]

**Output:** 2 

**Example 3:**

**Input:** nums = [7,8,9,11,12]

**Output:** 1 

**Constraints:**

*   <code>1 <= nums.length <= 5 * 10<sup>5</sup></code>
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>

To solve the "First Missing Positive" problem efficiently with O(n) time complexity and constant extra space, you can use the cyclic sort algorithm. Here's a step-by-step approach:

### Approach:

1. **Cyclic Sort:**
   - Perform cyclic sort on the given array `nums`.
   - Iterate through each number in the array and place it in its correct position if it is a positive integer and within the range of the array size.
   - Ignore negative numbers and numbers greater than the size of the array.
   - After cyclic sort, the array should contain positive integers starting from 1 to n, where n is the size of the array.

2. **Find the First Missing Positive:**
   - Iterate through the sorted array.
   - The first index where the value is not equal to its index plus one is the smallest missing positive integer.
   - If all numbers are in their correct positions, the smallest missing positive integer is the next integer after the array size.

### Python Code:

```python
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0

        while i < n:
            # If the number is positive and within the range of the array size,
            # and it's not already in its correct position, swap it to its correct position.
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        # Iterate through the sorted array to find the first missing positive integer.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers are in their correct positions, return the next positive integer.
        return n + 1

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [1, 2, 0]
print(solution.firstMissingPositive(nums1))  # Output: 3

# Example 2:
nums2 = [3, 4, -1, 1]
print(solution.firstMissingPositive(nums2))  # Output: 2

# Example 3:
nums3 = [7, 8, 9, 11, 12]
print(solution.firstMissingPositive(nums3))  # Output: 1
```

This code defines a `Solution` class with a `firstMissingPositive` method to find the smallest missing positive integer in the given unsorted array `nums`. The example usage demonstrates how to create an instance of the `Solution` class and call the `firstMissingPositive` method with different inputs.