78\. Subsets

Medium

Given an integer array `nums` of **unique** elements, return _all possible subsets (the power set)_.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

**Input:** nums = [1,2,3]

**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] 

**Example 2:**

**Input:** nums = [0]

**Output:** [[],[0]] 

**Constraints:**

*   `1 <= nums.length <= 10`
*   `-10 <= nums[i] <= 10`
*   All the numbers of `nums` are **unique**.

To solve the "Subsets" problem in Python with the Solution class, follow these steps:

1. Define a method `subsets` in the `Solution` class that takes an integer array `nums` as input and returns all possible subsets of `nums`.
2. Initialize an empty list to store the result subsets.
3. Implement a backtracking algorithm to generate all possible subsets:
   - Define a recursive helper function `generateSubsets` that takes the current subset, the current index in the array, and the array `nums` as parameters.
   - Base case: If the current index is equal to the length of `nums`, add the current subset to the result list.
   - Recursive case:
     - Include the current element in the subset and recursively call `generateSubsets` with the next index.
     - Exclude the current element from the subset and recursively call `generateSubsets` with the next index.
4. Call the `generateSubsets` function with an empty subset and the starting index 0.
5. Return the list containing all subsets.

Here's the implementation of the `subsets` method in Python:

```python
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(n + 1):
            for subset in combinations(nums, i):
                res.append(list(subset))
        return res

# Example usage:
# sol = Solution()
# result = sol.subsets([1, 2, 3])
# print(result)  # Output should be [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

This implementation uses backtracking to generate all possible subsets of the input array `nums`. It has a time complexity of O(2^N), where N is the number of elements in the input array.