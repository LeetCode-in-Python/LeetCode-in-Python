10\. Regular Expression Matching

Hard

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

*   `'.'` Matches any single character.
*   `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

**Example 1:**

**Input:** s = "aa", p = "a"

**Output:** false

**Explanation:** "a" does not match the entire string "aa". 

**Example 2:**

**Input:** s = "aa", p = "a\*"

**Output:** true

**Explanation:** '\*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa". 

**Example 3:**

**Input:** s = "ab", p = ".\*"

**Output:** true

**Explanation:** ".\*" means "zero or more (\*) of any character (.)". 

**Example 4:**

**Input:** s = "aab", p = "c\*a\*b"

**Output:** true

**Explanation:** c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab". 

**Example 5:**

**Input:** s = "mississippi", p = "mis\*is\*p\*."

**Output:** false 

**Constraints:**

*   `1 <= s.length <= 20`
*   `1 <= p.length <= 30`
*   `s` contains only lowercase English letters.
*   `p` contains only lowercase English letters, `'.'`, and `'*'`.
*   It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

Here are the steps for the recursive approach:

### Recursive Approach:

1. **Base Cases:**
   - If the pattern `p` is empty, the matching is successful if the string `s` is also empty. Return `True` if both are empty; otherwise, return `False`.
   - If the pattern `p` has only one character or the next character is not `'*'`, check if the first characters of `s` and `p` match. If yes, move to the next characters of both `s` and `p`; otherwise, return `False`.

2. **Handle '*' Character:**
   - If the next character in `p` is `'*'`, there are two possibilities:
     - Skip the `'*'` and the preceding character in `p` (i.e., match zero occurrences of the preceding character).
     - Match one occurrence of the preceding character in `p` with the current character in `s`.

3. **Recursive Calls:**
   - Recursively call the function with updated `s` and `p` for the possibilities mentioned in step 2.

4. **Return Result:**
   - Return `True` if any recursive call returns `True`; otherwise, return `False`.

### Python Code (Recursive):

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Base cases
        if not p:
            return not s

        first_match = bool(s) and (s[0] == p[0] or p[0] == '.')

        # Handle '*' character
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    (first_match and self.isMatch(s[1:], p)))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# Example Usage:
solution = Solution()

# Example 1:
s1, p1 = "aa", "a"
print(solution.isMatch(s1, p1))  # Output: False

# Example 2:
s2, p2 = "aa", "a*"
print(solution.isMatch(s2, p2))  # Output: True

# Example 3:
s3, p3 = "ab", ".*"
print(solution.isMatch(s3, p3))  # Output: True

# Example 4:
s4, p4 = "aab", "c*a*b"
print(solution.isMatch(s4, p4))  # Output: True

# Example 5:
s5, p5 = "mississippi", "mis*is*p*."
print(solution.isMatch(s5, p5))  # Output: False
```

This code defines a `Solution` class with a method `isMatch` that takes a string `s` and a pattern `p` as input and returns `True` if they match and `False` otherwise. The example usage demonstrates how to create an instance of the `Solution` class and call the `isMatch` method with different inputs using the recursive approach.