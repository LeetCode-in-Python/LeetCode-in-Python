20\. Valid Parentheses

Easy

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.

**Example 1:**

**Input:** s = "()"

**Output:** true 

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true 

**Example 3:**

**Input:** s = "(]"

**Output:** false 

**Example 4:**

**Input:** s = "([)]"

**Output:** false 

**Example 5:**

**Input:** s = "{[]}"

**Output:** true 

**Constraints:**

*   <code>1 <= s.length <= 10<sup>4</sup></code>
*   `s` consists of parentheses only `'()[]{}'`.

Here are the steps to solve the "Valid Parentheses" problem:

### Approach:

1. **Initialize Stack:**
   - Initialize an empty stack to keep track of the opening brackets.

2. **Iterate Through Characters:**
   - Iterate through each character in the input string `s`.

3. **Check for Opening Bracket:**
   - If the current character is an opening bracket (`'('`, `'{'`, or `'['`), push it onto the stack.

4. **Check for Closing Bracket:**
   - If the current character is a closing bracket (`')'`, `'}'`, or `']'`), check if the stack is empty. If it is, return `False` as there is no corresponding opening bracket.

5. **Check Matching Brackets:**
   - Pop the top element from the stack and check if it matches the corresponding opening bracket for the current closing bracket. If not, return `False`.

6. **Check for Empty Stack:**
   - After iterating through all characters, check if the stack is empty. If it is, return `True`; otherwise, return `False`.

### Python Code:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize stack
        stack = []

        # Define mapping of opening to closing brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}

        # Iterate through characters
        for char in s:
            # Check for opening bracket
            if char in bracket_mapping.values():
                stack.append(char)
            else:
                # Check for closing bracket
                if not stack or stack.pop() != bracket_mapping[char]:
                    return False

        # Check for empty stack
        return not stack

# Example Usage:
solution = Solution()

# Example 1:
input1 = "()"
result1 = solution.isValid(input1)  # Output: True

# Example 2:
input2 = "()[]{}"
result2 = solution.isValid(input2)  # Output: True

# Example 3:
input3 = "(]"
result3 = solution.isValid(input3)  # Output: False

# Example 4:
input4 = "([)]"
result4 = solution.isValid(input4)  # Output: False

# Example 5:
input5 = "{[]}"
result5 = solution.isValid(input5)  # Output: True
```

This code defines a `Solution` class with a method `isValid` that takes a string `s` as input and returns `True` if the parentheses in the input string are valid and `False` otherwise. The example usage demonstrates how to create an instance of the `Solution` class and call the `isValid` method with different inputs.