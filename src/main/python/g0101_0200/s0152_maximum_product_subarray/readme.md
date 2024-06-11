152\. Maximum Product Subarray

Medium

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return _the product_.

It is **guaranteed** that the answer will fit in a **32-bit** integer.

A **subarray** is a contiguous subsequence of the array.

**Example 1:**

**Input:** nums = [2,3,-2,4]

**Output:** 6

**Explanation:** [2,3] has the largest product 6. 

**Example 2:**

**Input:** nums = [-2,0,-1]

**Output:** 0

**Explanation:** The result cannot be 2, because [-2,-1] is not a subarray. 

**Constraints:**

*   <code>1 <= nums.length <= 2 * 10<sup>4</sup></code>
*   `-10 <= nums[i] <= 10`
*   The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

To solve the problem of finding the maximum product subarray, you can use a dynamic programming approach to keep track of the maximum and minimum products at each position in the array. This approach works because the product of two negative numbers can be positive, and thus the minimum product can become the maximum if a negative number is encountered.

Here are the detailed steps and the corresponding implementation in the `Solution` class:

### Steps:

1. **Initialization**:
   - Check if the input array `nums` is empty. If it is, return 0.
   - Initialize three variables:
     - `max_product` to keep track of the maximum product found so far.
     - `current_max` to keep track of the maximum product ending at the current position.
     - `current_min` to keep track of the minimum product ending at the current position.

2. **Iterate through the Array**:
   - Loop through each element in the array starting from the first element.
   - For each element, calculate the potential new values for `current_max` and `current_min` considering the current element itself, the product of `current_max` with the current element, and the product of `current_min` with the current element.
   - Update `current_max` to be the maximum of these values.
   - Update `current_min` to be the minimum of these values.
   - Update `max_product` to be the maximum of `max_product` and `current_max`.

3. **Return Result**:
   - After the loop, `max_product` will hold the maximum product of any subarray within `nums`.

### Implementation:

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                current_max, current_min = current_min, current_max
            
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            max_product = max(max_product, current_max)
        
        return max_product
```

### Explanation:

1. **Initialization**:
   - `max_product` is initialized to the first element of the array because the maximum product subarray must include at least one element.
   - `current_max` and `current_min` are also initialized to the first element.

2. **Iterate through the Array**:
   - For each element in `nums` (starting from the second element):
     - If the current element is negative, swap `current_max` and `current_min` because multiplying by a negative number flips the maximum and minimum.
     - Update `current_max` to be the maximum of the current element or the product of `current_max` with the current element.
     - Update `current_min` to be the minimum of the current element or the product of `current_min` with the current element.
     - Update `max_product` to be the maximum of `max_product` and `current_max`.

3. **Return Result**:
   - The `max_product` variable now contains the maximum product of any contiguous subarray.

This solution efficiently finds the maximum product subarray in O(n) time complexity with O(1) additional space complexity.