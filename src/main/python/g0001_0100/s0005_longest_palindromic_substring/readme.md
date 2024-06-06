5\. Longest Palindromic Substring

Medium

Given a string `s`, return _the longest palindromic substring_ in `s`.

**Example 1:**

**Input:** s = "babad"

**Output:** "bab" **Note:** "aba" is also a valid answer. 

**Example 2:**

**Input:** s = "cbbd"

**Output:** "bb" 

**Example 3:**

**Input:** s = "a"

**Output:** "a" 

**Example 4:**

**Input:** s = "ac"

**Output:** "a" 

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` consist of only digits and English letters.

Here are the steps to solve the "Longest Palindromic Substring" problem:

### Approach:

1. **Initialize Variables:**
   - Initialize two pointers, `start` and `end`, to represent the current substring being considered.
   - Initialize a variable `max_length` to store the length of the longest palindromic substring found.
   - Initialize variables `max_start` and `max_end` to store the starting and ending indices of the longest palindromic substring.

2. **Expand Around Center:**
   - Iterate through each character in the string `s`.
   - For each character, consider it as the center of a potential palindrome and expand around it to find the longest palindrome.

3. **Handle Odd-Length Palindromes:**
   - For each character, expand the substring by considering the current character as the center and expanding outward on both sides.
   - Update `start` and `end` pointers accordingly.

4. **Handle Even-Length Palindromes:**
   - Consider each pair of adjacent characters as potential centers and expand around them to find even-length palindromes.
   - Update `start` and `end` pointers accordingly.

5. **Update Longest Palindrome:**
   - After expanding around the current center, check if the length of the palindrome is greater than the current maximum (`max_length`).
   - If yes, update `max_length`, `max_start`, and `max_end`.

6. **Return Result:**
   - After iterating through all characters, return the longest palindromic substring using the indices `max_start` and `max_end`.

### Python Code:

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize variables
        max_length = 0
        max_start, max_end = 0, 0

        # Expand around center
        for i in range(len(s)):
            # Handle odd-length palindromes
            start, end = self.expand_around_center(s, i, i)
            if end - start + 1 > max_length:
                max_length = end - start + 1
                max_start, max_end = start, end

            # Handle even-length palindromes
            start, end = self.expand_around_center(s, i, i + 1)
            if end - start + 1 > max_length:
                max_length = end - start + 1
                max_start, max_end = start, end

        # Return the longest palindromic substring
        return s[max_start:max_end + 1]

    def expand_around_center(self, s, left, right):
        # Expand around center and return indices of the palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

# Example Usage:
solution = Solution()

# Example 1:
s1 = "babad"
print(solution.longestPalindrome(s1))  # Output: "bab" or "aba"

# Example 2:
s2 = "cbbd"
print(solution.longestPalindrome(s2))  # Output: "bb"

# Example 3:
s3 = "a"
print(solution.longestPalindrome(s3))  # Output: "a"

# Example 4:
s4 = "ac"
print(solution.longestPalindrome(s4))  # Output: "a"
```

This code defines a `Solution` class with a method `longestPalindrome` that takes a string `s` as input and returns the longest palindromic substring. The example usage demonstrates how to create an instance of the `Solution` class and call the `longestPalindrome` method with different inputs.