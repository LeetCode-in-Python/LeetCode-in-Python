49\. Group Anagrams

Medium

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]] 

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]] 

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]] 

**Constraints:**

*   <code>1 <= strs.length <= 10<sup>4</sup></code>
*   `0 <= strs[i].length <= 100`
*   `strs[i]` consists of lowercase English letters.

To solve the "Group Anagrams" problem, you can use a hash table to group the anagrams together based on their sorted representations. Here are the steps to solve the problem:

### Approach:

1. **Initialize a Hash Table:**
   - Initialize an empty dictionary to store the groups of anagrams. The keys of the dictionary will be the sorted representations of the words, and the values will be lists containing the original words.

2. **Iterate Through the Strings:**
   - Iterate through each string in the given array `strs`.

3. **Sort Each String:**
   - For each string, sort its characters alphabetically to get its sorted representation.

4. **Group Anagrams:**
   - Use the sorted representation as the key in the dictionary and append the original word to the corresponding list in the dictionary.

5. **Return the Groups:**
   - Return the values of the dictionary, which contain the groups of anagrams.

### Python Code:

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Initialize a dictionary to store groups of anagrams
        groups = defaultdict(list)
        
        # Group anagrams based on their sorted representations
        for word in strs:
            sorted_word = ''.join(sorted(word))
            groups[sorted_word].append(word)
        
        # Return the groups of anagrams
        return list(groups.values())

# Example Usage:
solution = Solution()

# Example 1:
strs1 = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs1))  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

# Example 2:
strs2 = [""]
print(solution.groupAnagrams(strs2))  # Output: [[""]]

# Example 3:
strs3 = ["a"]
print(solution.groupAnagrams(strs3))  # Output: [["a"]]
```

This code defines a `Solution` class with a `groupAnagrams` method to group the anagrams together. The example usage demonstrates how to create an instance of the `Solution` class and call the `groupAnagrams` method with different input arrays of strings.