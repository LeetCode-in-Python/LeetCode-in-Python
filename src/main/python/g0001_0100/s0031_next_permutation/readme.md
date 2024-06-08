31\. Next Permutation

Medium

Implement **next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be **[in place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.

**Example 1:**

**Input:** nums = [1,2,3]

**Output:** [1,3,2] 

**Example 2:**

**Input:** nums = [3,2,1]

**Output:** [1,2,3] 

**Example 3:**

**Input:** nums = [1,1,5]

**Output:** [1,5,1] 

**Example 4:**

**Input:** nums = [1]

**Output:** [1] 

**Constraints:**

*   `1 <= nums.length <= 100`
*   `0 <= nums[i] <= 100`

To solve the "Next Permutation" problem, you can use the following steps:

### Approach:

1. **Find the First Decreasing Element:**
   - Starting from the right, find the first pair of adjacent elements `nums[i]` and `nums[i+1]` where `nums[i] < nums[i+1]`. This element `nums[i]` is the first decreasing element.

2. **Find the Smallest Element to the Right of `nums[i]`:**
   - From the end, find the smallest element to the right of `nums[i]` that is greater than `nums[i]`. Let's call this element `nums[j]`.

3. **Swap `nums[i]` and `nums[j]`:**
   - Swap the elements `nums[i]` and `nums[j]`.

4. **Reverse the Subarray to the Right of `nums[i]`:**
   - Reverse the subarray to the right of `nums[i]` to ensure the smallest lexicographically next permutation.

### Python Code:

```python
class Solution:
    def nextPermutation(self, nums):
        # Step 1: Find the first decreasing element
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # Step 2: Find the smallest element to the right of nums[i] that is greater than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray to the right of nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [1, 2, 3]
solution.nextPermutation(nums1)  # Output: [1, 3, 2]

# Example 2:
nums2 = [3, 2, 1]
solution.nextPermutation(nums2)  # Output: [1, 2, 3]

# Example 3:
nums3 = [1, 1, 5]
solution.nextPermutation(nums3)  # Output: [1, 5, 1]

# Example 4:
nums4 = [1]
solution.nextPermutation(nums4)  # Output: [1]
```

This code defines a `Solution` class with a method `nextPermutation` that takes a list of integers `nums` and modifies it to the next lexicographically greater permutation. The example usage demonstrates how to create an instance of the `Solution` class and call the `nextPermutation` method with different inputs.