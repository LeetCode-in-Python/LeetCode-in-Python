76\. Minimum Window Substring

Hard

Given two strings `s` and `t` of lengths `m` and `n` respectively, return _the **minimum window substring** of_ `s` _such that every character in_ `t` _(**including duplicates**) is included in the window. If there is no such substring__, return the empty string_ `""`_._

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

**Input:** s = "ADOBECODEBANC", t = "ABC"

**Output:** "BANC"

**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t. 

**Example 2:**

**Input:** s = "a", t = "a"

**Output:** "a"

**Explanation:** The entire string s is the minimum window. 

**Example 3:**

**Input:** s = "a", t = "aa"

**Output:** ""

**Explanation:** Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string. 

**Constraints:**

*   `m == s.length`
*   `n == t.length`
*   <code>1 <= m, n <= 10<sup>5</sup></code>
*   `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

To solve the "Minimum Window Substring" problem in Python with the Solution class, follow these steps:

1. Define a method `minWindow` in the `Solution` class that takes two strings `s` and `t` as input and returns the minimum window substring of `s` containing all characters from `t`.
2. Create two frequency maps: `tFreqMap` to store the frequency of characters in string `t`, and `sFreqMap` to store the frequency of characters in the current window of string `s`.
3. Initialize two pointers `left` and `right` to track the window boundaries. Initialize a variable `minLength` to store the minimum window length found so far.
4. Iterate over string `s` using the `right` pointer until the end of the string:
   - Update the frequency map `sFreqMap` for the character at index `right`.
   - Check if the current window contains all characters from `t`. If it does, move the `left` pointer to minimize the window while maintaining the condition.
   - Update the `minLength` if the current window length is smaller.
   - Move the `right` pointer to expand the window.
5. Return the minimum window substring found, or an empty string if no such substring exists.

Here's the implementation of the `minWindow` method in Python:

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        map = [0] * 128
        for char in t:
            map[ord(char) - ord('A')] += 1

        count = len(t)
        begin = 0
        end = 0
        d = float('inf')
        head = 0

        while end < len(s):
            if map[ord(s[end]) - ord('A')] > 0:
                count -= 1
            map[ord(s[end]) - ord('A')] -= 1
            end += 1

            while count == 0:
                if end - begin < d:
                    d = end - begin
                    head = begin
                map[ord(s[begin]) - ord('A')] += 1
                if map[ord(s[begin]) - ord('A')] > 0:
                    count += 1
                begin += 1

        return "" if d == float('inf') else s[head:head + d]
        
# Example usage:
# sol = Solution()
# result = sol.minWindow("ADOBECODEBANC", "ABC")
# print(result)  # Output should be "BANC"
```

This implementation finds the minimum window substring in `O(m + n)` time complexity, where `m` is the length of string `s` and `n` is the length of string `t`. It uses two frequency maps to keep track of character frequencies and adjusts the window boundaries to find the minimum window containing all characters from `t`.