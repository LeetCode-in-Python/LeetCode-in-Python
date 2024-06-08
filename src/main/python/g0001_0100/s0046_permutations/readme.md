46\. Permutations

Medium

Given an array `nums` of distinct integers, return _all the possible permutations_. You can return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,2,3]

**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 

**Example 2:**

**Input:** nums = [0,1]

**Output:** [[0,1],[1,0]] 

**Example 3:**

**Input:** nums = [1]

**Output:** [[1]] 

**Constraints:**

*   `1 <= nums.length <= 6`
*   `-10 <= nums[i] <= 10`
*   All the integers of `nums` are **unique**.

To solve the "Permutations" problem, you can use backtracking. Here are the steps to solve the problem:

### Approach:

1. **Define Backtracking Function:**
   - Define a backtracking function `backtrack` to generate permutations recursively.
   - The function should take three parameters:
     - `path`: The current permutation being generated.
     - `nums`: The input array of distinct integers.
     - `result`: A list to store all permutations.

2. **Base Case:**
   - If the length of `path` equals the length of `nums`, append a copy of `path` to `result` and return.

3. **Recursive Step:**
   - Iterate through each element `num` in `nums`.
   - If `num` is not in `path`, append `num` to `path`.
   - Recur with the updated `path`.

4. **Generate Permutations:**
   - Call the backtracking function `backtrack` with an empty list `path`, the input array `nums`, and an empty list `result`.

5. **Return Result:**
   - After generating all permutations, return the `result` list.

### Python Code:

```python
class Solution:
    def permute(self, nums):
        def backtrack(path, nums, result):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path, nums, result)
                    path.pop()
        
        result = []
        backtrack([], nums, result)
        return result

# Example Usage:
solution = Solution()

# Example 1:
nums1 = [1,2,3]
print(solution.permute(nums1))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
nums2 = [0,1]
print(solution.permute(nums2))  # Output: [[0,1],[1,0]]

# Example 3:
nums3 = [1]
print(solution.permute(nums3))  # Output: [[1]]
```

This code defines a `Solution` class with a `permute` method to generate all possible permutations of the given array `nums`. The example usage demonstrates how to create an instance of the `Solution` class and call the `permute` method with different inputs.