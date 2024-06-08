39\. Combination Sum

Medium

Given an array of **distinct** integers `candidates` and a target integer `target`, return _a list of all **unique combinations** of_ `candidates` _where the chosen numbers sum to_ `target`_._ You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is **guaranteed** that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

**Example 1:**

**Input:** candidates = [2,3,6,7], target = 7

**Output:** [[2,2,3],[7]]

**Explanation:**

    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations. 

**Example 2:**

**Input:** candidates = [2,3,5], target = 8

**Output:** [[2,2,2,2],[2,3,3],[3,5]] 

**Example 3:**

**Input:** candidates = [2], target = 1

**Output:** [] 

**Example 4:**

**Input:** candidates = [1], target = 1

**Output:** [[1]] 

**Example 5:**

**Input:** candidates = [1], target = 2

**Output:** [[1,1]] 

**Constraints:**

*   `1 <= candidates.length <= 30`
*   `1 <= candidates[i] <= 200`
*   All elements of `candidates` are **distinct**.
*   `1 <= target <= 500`

To solve the Combination Sum problem, you can use backtracking. Here are the steps you can follow:

1. **Define the function**: Create a function, let's name it `combinationSum`, that takes `candidates`, `target`, and any other necessary parameters.

2. **Sort the candidates**: Sort the `candidates` array. Sorting helps in pruning the search space during backtracking.

3. **Initialize variables**: Initialize an empty list to store the result combinations. 

4. **Define a helper function**: Create a recursive helper function, let's name it `backtrack`, that takes the current combination, the current index of the candidate being considered, and the remaining target.

5. **Base case**: If the target is 0, add the current combination to the result list.

6. **Iterate through candidates**: Start iterating from the current index to the end of the `candidates` array.

7. **Check the sum condition**: For each candidate, check if adding it to the current combination keeps the sum less than or equal to the target. If so, recursively call the `backtrack` function with the updated combination, the current index, and the reduced target.

8. **Backtrack**: After the recursive call returns, remove the last element from the current combination to backtrack.

9. **Call the helper function**: Call the `backtrack` function initially with an empty combination, starting index 0, and the target.

10. **Return the result**: Return the list of combinations obtained.

Here's a Python code snippet implementing the above steps:

```python
class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result

# Test cases
solution = Solution()
print(solution.combinationSum([2,3,6,7], 7)) # Output: [[2, 2, 3], [7]]
print(solution.combinationSum([2,3,5], 8))   # Output: [[2, 2, 2, 2], [2, 3, 3], [5, 3]]
print(solution.combinationSum([2], 1))        # Output: []
print(solution.combinationSum([1], 1))        # Output: [[1]]
print(solution.combinationSum([1], 2))        # Output: [[1, 1]]
```

This implementation efficiently finds all unique combinations that sum up to the target.