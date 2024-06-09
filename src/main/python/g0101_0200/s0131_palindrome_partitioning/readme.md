131\. Palindrome Partitioning

Medium

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

A **palindrome** string is a string that reads the same backward as forward.

**Example 1:**

**Input:** s = "aab"

**Output:** [["a","a","b"],["aa","b"]] 

**Example 2:**

**Input:** s = "a"

**Output:** [["a"]] 

**Constraints:**

*   `1 <= s.length <= 16`
*   `s` contains only lowercase English letters.

To solve this task, we can use a backtracking approach. Here are the steps to solve the problem using the `Solution` class:

1. Define the `Solution` class with a method `partition` that takes a string `s` as input and returns a list of lists containing all possible palindrome partitions of `s`.
2. Within the `partition` method, initialize an empty list to store the result.
3. Define a helper function, let's name it `dfs`, which will perform depth-first search to generate all possible partitions.
4. In the `dfs` function, if the current partition `start` is equal to the length of the string `s`, append the current partition to the result list.
5. Otherwise, iterate through each possible end index of the substring starting from `start` to the end of the string.
6. Check if the substring from `start` to the current end index is a palindrome. If it is, recursively call the `dfs` function with the updated start index and add the current palindrome substring to the current partition.
7. After exploring all possible partitions, backtrack by removing the last added substring to explore other possibilities.
8. Finally, return the result list containing all possible palindrome partitions.

Here's how the `Solution` class would look like in Python:

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def dfs(start, partition):
            if start == len(s):
                result.append(partition[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    partition.append(s[start:end])
                    dfs(end, partition)
                    partition.pop()
        
        dfs(0, [])
        return result

# Example usage:
solution = Solution()
print(solution.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
print(solution.partition("a"))     # Output: [["a"]]
```

This solution utilizes backtracking to efficiently generate all possible palindrome partitions of the given string `s`.