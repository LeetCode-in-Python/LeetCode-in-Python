72\. Edit Distance

Hard

Given two strings `word1` and `word2`, return _the minimum number of operations required to convert `word1` to `word2`_.

You have the following three operations permitted on a word:

*   Insert a character
*   Delete a character
*   Replace a character

**Example 1:**

**Input:** word1 = "horse", word2 = "ros"

**Output:** 3

**Explanation:** horse -> rorse (replace 'h' with 'r') rorse -> rose (remove 'r') rose -> ros (remove 'e') 

**Example 2:**

**Input:** word1 = "intention", word2 = "execution"

**Output:** 5

**Explanation:** intention -> inention (remove 't') inention -> enention (replace 'i' with 'e') enention -> exention (replace 'n' with 'x') exention -> exection (replace 'n' with 'c') exection -> execution (insert 'u') 

**Constraints:**

*   `0 <= word1.length, word2.length <= 500`
*   `word1` and `word2` consist of lowercase English letters.

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `minDistance` that takes `word1` and `word2` as input parameters.
3. Implement the logic to calculate the minimum number of operations required to convert `word1` to `word2` using dynamic programming.
4. Create a 2D array `dp` of size `(len(word1) + 1) x (len(word2) + 1)` to store the minimum number of operations required to convert substrings of `word1` to substrings of `word2`.
5. Initialize the first row and first column of `dp` to represent the base cases: the minimum number of operations required to convert an empty string to a string of length `i` or `j` is equal to `i` or `j` respectively.
6. Iterate through the substrings of `word1` and `word2` and fill in the `dp` array using the following recurrence relation:
   - If the characters at the current positions are equal, `dp[i][j] = dp[i-1][j-1]`.
   - Otherwise, `dp[i][j]` is the minimum of the following:
     - `1 + dp[i-1][j]` (delete operation)
     - `1 + dp[i][j-1]` (insert operation)
     - `1 + dp[i-1][j-1]` (replace operation)
7. Return `dp[len(word1)][len(word2)]`, which represents the minimum number of operations required to convert `word1` to `word2`.

Here's the implementation:

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the first row and first column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Calculate the minimum number of operations
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]

# Example usage:
solution = Solution()
print(solution.minDistance("horse", "ros"))  # Output: 3
print(solution.minDistance("intention", "execution"))  # Output: 5
```

This implementation uses dynamic programming to efficiently calculate the minimum number of operations required. It iterates through the substrings of `word1` and `word2` only once, so the time complexity is O(m * n), where m is the length of `word1` and n is the length of `word2`.