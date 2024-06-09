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

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `subsets` that takes `nums` as an input parameter.
3. Implement an algorithm to generate all possible subsets of the given array `nums`.
4. Use backtracking to generate all possible combinations of elements in `nums`.
5. Create an empty list `result` to store the subsets.
6. Define a recursive function named `generate` that takes `start` (starting index), `subset` (current subset), and `result` (list of subsets) as parameters.
7. Base case: If `start` is equal to the length of `nums`, append a copy of `subset` to `result` and return.
8. Recursive case: For each index `i` starting from `start`, append `nums[i]` to `subset`, recursively call `generate` with `i + 1`, `subset`, and `result`, then backtrack by removing the last element from `subset`.
9. After backtracking, call `generate` with `start + 1`, `subset`, and `result` to explore other possibilities.
10. After the recursive calls, return `result`.
11. Call the `generate` function initially with `start = 0`, an empty list `subset`, and the `result` list.
12. Return the `result` list containing all possible subsets.

Here's the implementation:

```python
class Solution:
    def subsets(self, nums):
        def generate(start, subset, result):
            if start == len(nums):
                result.append(subset[:])
                return
            
            generate(start + 1, subset, result)
            subset.append(nums[start])
            generate(start + 1, subset, result)
            subset.pop()
        
        result = []
        generate(0, [], result)
        return result

# Example usage:
solution = Solution()
print(solution.subsets([1, 2, 3]))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(solution.subsets([0]))         # Output: [[], [0]]
```

This solution generates all possible subsets using backtracking. It explores all possible combinations of elements in the array `nums`, resulting in a time complexity of O(2^n), where n is the number of elements in `nums`.