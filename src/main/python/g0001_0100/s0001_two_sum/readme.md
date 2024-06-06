1\. Two Sum

Easy

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

**Example 1:**

**Input:** nums = [2,7,11,15], target = 9

**Output:** [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]. 

**Example 2:**

**Input:** nums = [3,2,4], target = 6

**Output:** [1,2] 

**Example 3:**

**Input:** nums = [3,3], target = 6

**Output:** [0,1] 

**Constraints:**

*   <code>2 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>
*   <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code>
*   **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code> time complexity?

Here are the steps to solve the Two Sum problem:

### Approach:

1. **Create a Dictionary/HashMap:**
   - Initialize an empty dictionary to store the elements of the array and their corresponding indices.

2. **Iterate through the Array:**
   - Traverse through the given array `nums` using a loop.

3. **Check Complement:**
   - For each element `nums[i]`, calculate its complement (i.e., `target - nums[i]`).

4. **Check if Complement exists:**
   - Check if the complement is already in the dictionary.
     - If it is, return the indices `[dictionary[complement], i]`.
     - If not, add the current element and its index to the dictionary.

### Python Code:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store elements and their indices
        num_dict = {}
        
        # Iterate through the array
        for i in range(len(nums)):
            # Check complement
            complement = target - nums[i]
            
            # Check if complement exists in the dictionary
            if complement in num_dict:
                # Return the indices if complement is found
                return [num_dict[complement], i]
            
            # Add the current element and its index to the dictionary
            num_dict[nums[i]] = i
        
        # If no solution is found
        return None

# Example Usage:
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
```

### Time Complexity:
The time complexity of this algorithm is O(n), where n is the number of elements in the array. The dictionary lookup operation is constant time.