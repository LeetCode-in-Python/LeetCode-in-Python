45\. Jump Game II

Medium

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

**Example 1:**

**Input:** nums = [2,3,1,1,4]

**Output:** 2

**Explanation:** The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index. 

**Example 2:**

**Input:** nums = [2,3,0,1,4]

**Output:** 2 

**Constraints:**

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   `0 <= nums[i] <= 1000`

To solve the "Jump Game II" problem efficiently, you can use a greedy approach. Here are the steps to solve the problem:

### Approach:

1. **Initialize Variables:**
   - Initialize variables `max_reach` to store the farthest index that can be reached from the current position.
   - Initialize variables `steps` to store the minimum number of jumps needed to reach the current position.
   - Initialize variables `last_jump` to store the index where the last jump was made.

2. **Iterate Through Array:**
   - Iterate through the array `nums` up to the second last index.
   - For each index `i`:
     - Update `max_reach` to the maximum of `max_reach` and `i + nums[i]`.
     - If `i` reaches the `last_jump` index, update `last_jump` to `max_reach` and increment `steps`.

3. **Return Result:**
   - After the loop ends, return the `steps` variable, which contains the minimum number of jumps needed to reach the last index.

### Python Code:

```python
class Solution:
    def jump(self, nums):
        n = len(nums)
        max_reach = last_jump = steps = 0
        
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == last_jump:
                last_jump = max_reach
                steps += 1
                
        return steps

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [2,3,1,1,4]
print(solution.jump(nums1))  # Output: 2

# Example 2:
nums2 = [2,3,0,1,4]
print(solution.jump(nums2))  # Output: 2
```

This code defines a `Solution` class with a `jump` method to compute the minimum number of jumps needed to reach the last index in the given array `nums`. The example usage demonstrates how to create an instance of the `Solution` class and call the `jump` method with different inputs.