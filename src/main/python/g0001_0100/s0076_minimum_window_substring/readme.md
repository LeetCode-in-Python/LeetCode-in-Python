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

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `minWindow` that takes `s` and `t` as input parameters.
3. Implement an algorithm to find the minimum window substring of `s` that contains all characters of `t`.
4. Use a sliding window approach to efficiently search for the minimum window substring.
5. Create a dictionary `t_count` to store the frequency of characters in string `t`.
6. Initialize variables `left` and `right` to keep track of the window boundaries.
7. Initialize variables `min_window_start` and `min_window_length` to store the starting index and length of the minimum window substring found so far.
8. Iterate through string `s` using the right pointer (`right`), and update the character frequencies in a temporary dictionary `window_count`.
9. When all characters of `t` are found in the current window, update `min_window_start` and `min_window_length` if the current window is smaller than the minimum window found so far.
10. Move the left pointer (`left`) to shrink the window until the window no longer contains all characters of `t`.
11. Repeat steps 8-10 until the right pointer reaches the end of `s`.
12. Return the minimum window substring found, or an empty string if no such substring exists.

Here's the implementation:

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        left, right = 0, 0
        min_window_start = 0
        min_window_length = float('inf')
        required_chars = len(t)
        
        while right < len(s):
            if s[right] in t_count:
                if t_count[s[right]] > 0:
                    required_chars -= 1
                t_count[s[right]] -= 1
            
            while required_chars == 0:
                if right - left + 1 < min_window_length:
                    min_window_length = right - left + 1
                    min_window_start = left
                
                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] > 0:
                        required_chars += 1
                left += 1
            
            right += 1
        
        return s[min_window_start:min_window_start + min_window_length] if min_window_length != float('inf') else ""
```

This solution uses a sliding window approach to efficiently search for the minimum window substring. It iterates through the string `s` only once, so the time complexity is O(m + n), where m is the length of `s` and n is the length of `t`.