32\. Longest Valid Parentheses

Hard

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

**Example 1:**

**Input:** s = "(()"

**Output:** 2

**Explanation:** The longest valid parentheses substring is "()". 

**Example 2:**

**Input:** s = ")()())"

**Output:** 4

**Explanation:** The longest valid parentheses substring is "()()". 

**Example 3:**

**Input:** s = ""

**Output:** 0 

**Constraints:**

*   <code>0 <= s.length <= 3 * 10<sup>4</sup></code>
*   `s[i]` is `'('`, or `')'`.

To solve the "Longest Valid Parentheses" problem, you can use the following steps:

### Approach:

1. **Initialize Variables:**
   - Initialize a variable `max_length` to store the maximum valid parentheses substring length.
   - Initialize a stack to keep track of indices of opening parentheses.

2. **Traverse the String:**
   - Iterate through each character in the string.
   - If the character is `'('`, push its index onto the stack.
   - If the character is `')'`:
     - If the stack is not empty, pop an element from the stack.
     - If the stack becomes empty:
       - Push the current index onto the stack (marks the start of a potential new valid substring).
       - Update `max_length` using the difference between the current index and the index popped from the stack.
     - If the stack is not empty, update `max_length` using the difference between the current index and the index at the top of the stack.

3. **Final Result:**
   - The value of `max_length` will represent the length of the longest valid parentheses substring.

### Python Code:

```python
class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]  # Initialize the stack with -1 to handle the case when the first parenthesis is ')'
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # s[i] == ')'
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length

# Example Usage:
solution = Solution()

# Example 1:
s1 = "(()"
print(solution.longestValidParentheses(s1))  # Output: 2

# Example 2:
s2 = ")()())"
print(solution.longestValidParentheses(s2))  # Output: 4

# Example 3:
s3 = ""
print(solution.longestValidParentheses(s3))  # Output: 0
```

This code defines a `Solution` class with a method `longestValidParentheses` that takes a string `s` and returns the length of the longest valid parentheses substring. The example usage demonstrates how to create an instance of the `Solution` class and call the `longestValidParentheses` method with different inputs.