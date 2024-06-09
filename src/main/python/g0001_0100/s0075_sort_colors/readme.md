75\. Sort Colors

Medium

Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

**Example 1:**

**Input:** nums = [2,0,2,1,1,0]

**Output:** [0,0,1,1,2,2] 

**Example 2:**

**Input:** nums = [2,0,1]

**Output:** [0,1,2] 

**Example 3:**

**Input:** nums = [0]

**Output:** [0] 

**Example 4:**

**Input:** nums = [1]

**Output:** [1] 

**Constraints:**

*   `n == nums.length`
*   `1 <= n <= 300`
*   `nums[i]` is `0`, `1`, or `2`.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `sortColors` that takes `nums` as an input parameter.
3. Implement the one-pass algorithm to sort the colors in-place.
4. Use three pointers: `left`, `right`, and `curr`.
5. Initialize `left` to 0, `right` to `len(nums) - 1`, and `curr` to 0.
6. Iterate through the array while `curr` is less than or equal to `right`.
7. If `nums[curr]` is 0, swap `nums[curr]` with `nums[left]`, increment both `left` and `curr`.
8. If `nums[curr]` is 2, swap `nums[curr]` with `nums[right]`, decrement `right`.
9. If `nums[curr]` is 1, simply increment `curr`.
10. Repeat steps 6-9 until `curr` is greater than `right`.

Here's the implementation:

```python
class Solution:
    def sortColors(self, nums):
        left, right, curr = 0, len(nums) - 1, 0
        
        while curr <= right:
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

# Example usage:
solution = Solution()
nums1 = [2,0,2,1,1,0]
solution.sortColors(nums1)
print(nums1)  # Output: [0,0,1,1,2,2] 

nums2 = [2,0,1]
solution.sortColors(nums2)
print(nums2)  # Output: [0,1,2] 

nums3 = [0]
solution.sortColors(nums3)
print(nums3)  # Output: [0] 

nums4 = [1]
solution.sortColors(nums4)
print(nums4)  # Output: [1] 
```

This solution sorts the colors in-place using a one-pass algorithm with constant extra space. It traverses the array only once, so the time complexity is O(n), where n is the length of the array `nums`.