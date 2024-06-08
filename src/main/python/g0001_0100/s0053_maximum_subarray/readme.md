53\. Maximum Subarray

Easy

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return _its sum_.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]

**Output:** 6

**Explanation:** [4,-1,2,1] has the largest sum = 6. 

**Example 2:**

**Input:** nums = [1]

**Output:** 1 

**Example 3:**

**Input:** nums = [5,4,-1,7,8]

**Output:** 23 

**Constraints:**

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

To solve the Maximum Subarray problem, we can use the Kadane's algorithm, which efficiently finds the maximum subarray sum in linear time. Here are the steps to solve the task:

1. **Initialize Variables:** 
   - Initialize two variables `max_sum` and `current_sum` to keep track of the maximum sum found so far and the sum of the current subarray, respectively.
   - Set `max_sum` and `current_sum` to the value of the first element in the array `nums`.

2. **Iterate Through the Array:**
   - Start iterating through the array `nums` from the second element (index 1).
   - For each element `num` in `nums`, do the following:
     - Update `current_sum` to be the maximum of either `num` or `current_sum + num`. This step ensures that we consider either starting a new subarray or extending the current subarray.
     - Update `max_sum` to be the maximum of either `max_sum` or `current_sum`. This step ensures that we keep track of the maximum subarray sum found so far.

3. **Return the Result:**
   - After iterating through the entire array, `max_sum` will contain the maximum subarray sum.
   - Return `max_sum` as the result.

### Python Implementation:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables
        max_sum = current_sum = nums[0]

        # Iterate through the array
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

# Example Usage:
solution = Solution()
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums1))  # Output: 6

nums2 = [1]
print(solution.maxSubArray(nums2))  # Output: 1

nums3 = [5, 4, -1, 7, 8]
print(solution.maxSubArray(nums3))  # Output: 23
```

This algorithm has a time complexity of O(n), where n is the length of the input array `nums`. Therefore, it efficiently finds the maximum subarray sum.