70\. Climbing Stairs

Easy

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

**Input:** n = 2

**Output:** 2

**Explanation:** There are two ways to climb to the top. 1. 1 step + 1 step 2. 2 steps 

**Example 2:**

**Input:** n = 3

**Output:** 3

**Explanation:** There are three ways to climb to the top. 1. 1 step + 1 step + 1 step 2. 1 step + 2 steps 3. 2 steps + 1 step 

**Constraints:**

*   `1 <= n <= 45`

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `climbStairs` that takes `n` as an input parameter.
3. Implement the logic to calculate the number of distinct ways to climb to the top using dynamic programming.
4. Create a list `dp` to store the number of distinct ways to reach each step.
5. Initialize `dp[0]`, `dp[1]`, and `dp[2]` to 1, 1, and 2 respectively, as there is only one way to reach the first two steps, and two ways to reach the third step.
6. Iterate through the range from 3 to `n`, updating each element of `dp` using the formula `dp[i] = dp[i-1] + dp[i-2]`.
7. Return `dp[n]`, which represents the number of distinct ways to climb to the top.

Here's the implementation:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a list to store the number of distinct ways to reach each step
        dp = [0] * (n + 1)
        
        # Initialize the first two steps
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        # Calculate the number of distinct ways for each step
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return the number of distinct ways to climb to the top
        return dp[n]

# Example usage:
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
```

This implementation uses dynamic programming to efficiently calculate the number of distinct ways to climb to the top. It iterates through the steps only once, so the time complexity is O(n), where n is the number of steps.