15\. 3Sum

Medium

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

**Input:** nums = [-1,0,1,2,-1,-4]

**Output:** [[-1,-1,2],[-1,0,1]] 

**Example 2:**

**Input:** nums = []

**Output:** [] 

**Example 3:**

**Input:** nums = [0]

**Output:** [] 

**Constraints:**

*   `0 <= nums.length <= 3000`
*   <code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code>

Here are the steps to solve the "3Sum" problem:

### Approach:

1. **Sort the Array:**
   - Sort the given array `nums` in ascending order.

2. **Initialize Result List:**
   - Initialize an empty list `result` to store the triplets.

3. **Iterate Through the Array:**
   - Iterate through the sorted array `nums` from index `i = 0` to `i = len(nums) - 3`.

4. **Check for Duplicate Elements:**
   - If the current element is the same as the previous element, skip to the next iteration to avoid duplicate triplets.

5. **Use Two Pointers for 2Sum:**
   - Use two pointers (`left` and `right`) to find a pair of elements whose sum is equal to the negation of the current element (`-nums[i]`).
     - Initialize `left = i + 1` and `right = len(nums) - 1`.
     - Check if `nums[i] + nums[left] + nums[right] == 0`.

6. **Move Pointers:**
   - If the sum is less than zero, increment `left`.
   - If the sum is greater than zero, decrement `right`.
   - If the sum is zero, add the triplet `[nums[i], nums[left], nums[right]]` to the result list.

7. **Skip Duplicate Elements:**
   - While moving pointers, skip duplicate elements to avoid duplicate triplets.

8. **Return Result:**
   - Return the final list of triplets.

### Python Code:

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()
        result = []

        # Iterate through the array
        for i in range(len(nums) - 2):
            # Check for duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers for 2Sum
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Add triplet to result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers
                    left += 1
                    right -= 1

        return result

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

# Example 2:
nums2 = []
print(solution.threeSum(nums2))  # Output: []

# Example 3:
nums3 = [0]
print(solution.threeSum(nums3))  # Output: []
```

This code defines a `Solution` class with a method `threeSum` that takes an array `nums` as input and returns a list of unique triplets whose sum is equal to zero. The example usage demonstrates how to create an instance of the `Solution` class and call the `threeSum` method with different inputs.