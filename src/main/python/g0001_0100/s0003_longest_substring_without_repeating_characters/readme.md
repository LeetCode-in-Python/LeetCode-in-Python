3\. Longest Substring Without Repeating Characters

Medium

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**

**Input:** s = "abcabcbb"

**Output:** 3

**Explanation:** The answer is "abc", with the length of 3. 

**Example 2:**

**Input:** s = "bbbbb"

**Output:** 1

**Explanation:** The answer is "b", with the length of 1. 

**Example 3:**

**Input:** s = "pwwkew"

**Output:** 3

**Explanation:** The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. 

**Example 4:**

**Input:** s = ""

**Output:** 0 

**Constraints:**

*   <code>0 <= s.length <= 5 * 10<sup>4</sup></code>
*   `s` consists of English letters, digits, symbols and spaces.

Here are the steps to solve the "Longest Substring Without Repeating Characters" problem:

### Approach:

1. **Initialize Pointers and Variables:**
   - Initialize two pointers, `start` and `end`, to define the current substring.
   - Initialize a dictionary `char_index` to store the last index of each character in the substring.
   - Initialize the variable `max_length` to track the length of the longest substring.

2. **Traverse the String:**
   - Use the `end` pointer to traverse through the string `s`.

3. **Check for Repeating Characters:**
   - If the character at the current `end` pointer is not in the substring (not in `char_index`), add it to the substring.
   - Update `max_length` if the length of the current substring is greater than the previous maximum.

4. **Adjust Start Pointer:**
   - If the character is already in the substring, move the `start` pointer to the right of the last occurrence of that character.
   - This ensures that the substring does not contain repeating characters.

5. **Update Character Index:**
   - Update the index of the current character in the `char_index` dictionary.

6. **Repeat Until End of String:**
   - Repeat steps 3-5 until the `end` pointer reaches the end of the string.

7. **Return Maximum Length:**
   - The maximum length of the substring without repeating characters is stored in the variable `max_length`.

### Python Code:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize pointers and variables
        start, end = 0, 0
        char_index = {}  # Dictionary to store the last index of each character
        max_length = 0

        # Traverse the string
        while end < len(s):
            # Check for repeating characters
            if s[end] not in char_index or char_index[s[end]] < start:
                # Update max_length
                max_length = max(max_length, end - start + 1)
            else:
                # Adjust start pointer
                start = char_index[s[end]] + 1

            # Update character index
            char_index[s[end]] = end

            # Move end pointer to the next character
            end += 1

        # Return the maximum length of the substring
        return max_length

# Example Usage:
solution = Solution()

# Example 1:
s1 = "abcabcbb"
gprint(solution.lengthOfLongestSubstring(s1))  # Output: 3

# Example 2:
s2 = "bbbbb"
print(solution.lengthOfLongestSubstring(s2))  # Output: 1

# Example 3:
s3 = "pwwkew"
print(solution.lengthOfLongestSubstring(s3))  # Output: 3

# Example 4:
s4 = ""
print(solution.lengthOfLongestSubstring(s4))  # Output: 0
```

This code defines a `Solution` class with a method `lengthOfLongestSubstring` that takes a string `s` as input and returns the length of the longest substring without repeating characters. The example usage demonstrates how to create an instance of the `Solution` class and call the `lengthOfLongestSubstring` method with different inputs.