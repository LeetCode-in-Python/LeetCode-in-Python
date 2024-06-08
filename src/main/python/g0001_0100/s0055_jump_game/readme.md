55\. Jump Game

Medium

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` _if you can reach the last index, or_ `false` _otherwise_.

**Example 1:**

**Input:** nums = [2,3,1,1,4]

**Output:** true

**Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index. 

**Example 2:**

**Input:** nums = [3,2,1,0,4]

**Output:** false

**Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index. 

**Constraints:**

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>0 <= nums[i] <= 10<sup>5</sup></code>

To solve the "Jump Game" problem, you can follow these steps:

1. **Initialize Variables:** Start by initializing a variable `max_reach` to store the maximum reachable index. Initially, set `max_reach` to `0`, as you are at the first index.
   
2. **Iterate through the Array:** Traverse through the array `nums` starting from index `0` to `n-1`, where `n` is the length of the array.

3. **Update Maximum Reach:** At each index `i`, update `max_reach` to be the maximum of `max_reach` and `i + nums[i]`. This indicates the farthest index you can reach from the current position `i`.

4. **Check for End Reachability:** While traversing the array, if at any point `max_reach` becomes greater than or equal to the last index (i.e., `n - 1`), return `True`, indicating that you can reach the end of the array.

5. **Handle Zero Reach:** If the current index `i` is greater than `max_reach`, it means you cannot progress further, and thus, return `False`.

6. **Return Result:** After iterating through the entire array, if you haven't reached the end of the array, return `False`, as you cannot reach the last index.

Here's a Python function implementing the above steps:

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)
        
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        
        return False

# Example usage:
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

sol = Solution()
print(sol.canJump(nums1))  # Output: True
print(sol.canJump(nums2))  # Output: False
```

You can then test this function with different input arrays to verify its correctness.