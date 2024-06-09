96\. Unique Binary Search Trees

Medium

Given an integer `n`, return _the number of structurally unique **BST'**s (binary search trees) which has exactly_ `n` _nodes of unique values from_ `1` _to_ `n`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)

**Input:** n = 3

**Output:** 5 

**Example 2:**

**Input:** n = 1

**Output:** 1 

**Constraints:**

*   `1 <= n <= 19`

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `numTrees` that takes `n` as an input parameter.
3. Implement an algorithm to calculate the number of structurally unique BSTs (binary search trees) with exactly `n` nodes.
4. Use dynamic programming to efficiently compute the number of unique BSTs.
5. Create a list `dp` of length `n + 1` to store the number of unique BSTs for each number of nodes from 0 to `n`.
6. Initialize `dp[0]` and `dp[1]` to 1, as there is only one unique BST for empty tree or tree with only one node.
7. Iterate from 2 to `n`:
    - For each `i`, calculate `dp[i]` by summing up the products of `dp[j - 1]` and `dp[i - j]` for all possible values of `j` from 1 to `i`.
8. Return `dp[n]` as the result.

Here's the implementation:

```python
class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]

# Example usage:
solution = Solution()
print(solution.numTrees(3))  # Output: 5
print(solution.numTrees(1))  # Output: 1
```

This solution efficiently calculates the number of structurally unique BSTs using dynamic programming. It iterates through each number of nodes from 2 to `n` and computes the number of unique BSTs for each number of nodes, resulting in a time complexity of O(n^2).