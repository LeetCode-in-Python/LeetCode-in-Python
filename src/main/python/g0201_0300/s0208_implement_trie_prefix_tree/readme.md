208\. Implement Trie (Prefix Tree)

Medium

A [**trie**](https://en.wikipedia.org/wiki/Trie) (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

*   `Trie()` Initializes the trie object.
*   `void insert(String word)` Inserts the string `word` into the trie.
*   `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
*   `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Example 1:**

**Input**

    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

**Output:** [null, null, true, false, true, null, true]

**Explanation:**

    Trie trie = new Trie();
    trie.insert("apple"); trie.search("apple"); // return True
    trie.search("app"); // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app"); // return True 

**Constraints:**

*   `1 <= word.length, prefix.length <= 2000`
*   `word` and `prefix` consist only of lowercase English letters.
*   At most <code>3 * 10<sup>4</sup></code> calls **in total** will be made to `insert`, `search`, and `startsWith`.

To solve the task, here are the steps for implementing the Trie (Prefix Tree) problem:

1. **Define the TrieNode Class**:
   - Define a class named `TrieNode` to represent each node in the trie.
   - Each node will have a dictionary to store child nodes, indicating possible characters that can follow the current node.
   - Additionally, each node will have a boolean flag to mark whether it represents the end of a word.

2. **Initialize the Trie Class**:
   - Implement the `__init__` method for the Trie class to initialize an empty trie with a root node.

3. **Implement the Insert Method**:
   - Implement the `insert` method to insert a word into the trie.
   - Start from the root node and iterate through each character in the word.
   - Check if the character exists as a child of the current node. If not, create a new node for it.
   - Move to the child node and repeat the process for the next character.
   - After processing all characters, mark the last node as the end of the word.

4. **Implement the Search Method**:
   - Implement the `search` method to check if a word exists in the trie.
   - Start from the root node and iterate through each character in the word.
   - If at any point, a character is not found as a child of the current node, return False.
   - If all characters are found and the last node is marked as the end of a word, return True.

5. **Implement the StartsWith Method**:
   - Implement the `startsWith` method to check if there is any word in the trie that starts with a given prefix.
   - Follow a similar process as the search method, but return True as soon as all characters of the prefix are found, regardless of whether it forms a complete word.

6. **Return Results**:
   - After implementing all methods, create an instance of the Trie class and perform the required operations according to the given input.

Here's a Python implementation:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example Usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple")) # Output: True
print(trie.search("app")) # Output: False
print(trie.startsWith("app")) # Output: True
trie.insert("app")
print(trie.search("app")) # Output: True
``` 

This solution efficiently implements the Trie data structure and satisfies the requirements of the problem.