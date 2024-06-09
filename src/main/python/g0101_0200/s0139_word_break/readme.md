139\. Word Break

Medium

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**

**Input:** s = "leetcode", wordDict = ["leet","code"]

**Output:** true

**Explanation:** Return true because "leetcode" can be segmented as "leet code". 

**Example 2:**

**Input:** s = "applepenapple", wordDict = ["apple","pen"]

**Output:** true

**Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word. 

**Example 3:**

**Input:** s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]

**Output:** false 

**Constraints:**

*   `1 <= s.length <= 300`
*   `1 <= wordDict.length <= 1000`
*   `1 <= wordDict[i].length <= 20`
*   `s` and `wordDict[i]` consist of only lowercase English letters.
*   All the strings of `wordDict` are **unique**.

To solve this problem with the `Solution` class, we can use dynamic programming to efficiently determine whether the string `s` can be segmented into words from the dictionary `wordDict`. Here are the steps:

1. Define the `Solution` class with a method `wordBreak` that takes a string `s` and a list of strings `wordDict` as input and returns a boolean indicating whether `s` can be segmented into words from `wordDict`.
2. Initialize a boolean list `dp` of size `len(s) + 1`, where `dp[i]` represents whether the substring `s[:i]` can be segmented into words from `wordDict`.
3. Set `dp[0]` to `True` since an empty string can always be segmented.
4. Iterate `i` from 1 to `len(s)`, and for each index `i`, iterate `j` from 0 to `i`.
5. Check if the substring `s[j:i]` exists in `wordDict` and if `dp[j]` is `True`. If both conditions are met, set `dp[i]` to `True`.
6. After completing the iterations, return `dp[len(s)]`, which represents whether the entire string `s` can be segmented into words from `wordDict`.

Here's how the `Solution` class would look like in Python:

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

# Example usage:
solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))         # Output: True
print(solution.wordBreak("applepenapple", ["apple", "pen"]))    # Output: True
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
```

This solution effectively utilizes dynamic programming to determine whether the string `s` can be segmented into words from the dictionary `wordDict`, satisfying the constraints provided in the problem statement.