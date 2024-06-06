22\. Generate Parentheses

Medium

Given `n` pairs of parentheses, write a function to _generate all combinations of well-formed parentheses_.

**Example 1:**

**Input:** n = 3

**Output:** ["((()))","(()())","(())()","()(())","()()()"] 

**Example 2:**

**Input:** n = 1

**Output:** ["()"] 

**Constraints:**

*   `1 <= n <= 8`

Here are the steps to solve the "Generate Parentheses" problem:

### Approach:

1. **Initialize Result List:**
   - Initialize an empty list `result` to store the generated combinations.

2. **Define Recursive Function:**
   - Define a recursive function `generateParenthesisHelper` that takes parameters:
     - `current`: the current combination being built.
     - `left`: the remaining count of open parentheses.
     - `right`: the remaining count of close parentheses.

3. **Base Case:**
   - If both `left` and `right` become zero, add the current combination to the `result` list.

4. **Recursive Calls:**
   - If `left` is greater than zero, make a recursive call with one less open parenthesis and the current combination appended with an open parenthesis.
   - If `right` is greater than `left`, make a recursive call with one less close parenthesis and the current combination appended with a close parenthesis.

5. **Initialize:**
   - Start the recursion by calling the `generateParenthesisHelper` function with an empty string (`current`), the total number of open parentheses (`n`), and the total number of close parentheses (`n`).

6. **Return Result:**
   - Return the `result` list containing all the valid combinations.

### Python Code:

```python
class Solution:
    def generateParenthesis(self, n: int):
        def generateParenthesisHelper(current, left, right):
            # Base case: If both left and right are zero, add the current combination to result
            if left == 0 and right == 0:
                result.append(current)
                return
            # Recursive calls
            if left > 0:
                generateParenthesisHelper(current + '(', left - 1, right)
            if right > left:
                generateParenthesisHelper(current + ')', left, right - 1)

        # Initialize result list
        result = []
        # Start recursion
        generateParenthesisHelper('', n, n)
        # Return result list
        return result

# Example Usage:
solution = Solution()

# Example 1:
n1 = 3
result1 = solution.generateParenthesis(n1)  # Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
n2 = 1
result2 = solution.generateParenthesis(n2)  # Output: ["()"]
```

This code defines a `Solution` class with a method `generateParenthesis` that takes an integer `n` as input and returns a list containing all combinations of well-formed parentheses for `n` pairs. The example usage demonstrates how to create an instance of the `Solution` class and call the `generateParenthesis` method with different inputs.