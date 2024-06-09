# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Hash_Table #Design #Trie
# #Level_2_Day_16_Design #Udemy_Trie_and_Heap
# #Big_O_Time_O(word.length())_or_O(prefix.length())_Space_O(N)
# #2024_06_09_Time_140_ms_(28.87%)_Space_33.8_MB_(16.61%)

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.startWith = False

    # Inserts a word into the trie.
    def insert(self, word):
        self._insert(word, self.root, 0)

    def _insert(self, word, root, idx):
        if idx == len(word):
            root.isWord = True
            return
        index = ord(word[idx]) - ord('a')
        if root.children[index] is None:
            root.children[index] = TrieNode()
        self._insert(word, root.children[index], idx + 1)

    # Returns if the word is in the trie.
    def search(self, word):
        return self._search(word, self.root, 0)

    def _search(self, word, root, idx):
        if idx == len(word):
            self.startWith = True
            return root.isWord
        index = ord(word[idx]) - ord('a')
        if root.children[index] is None:
            self.startWith = False
            return False
        return self._search(word, root.children[index], idx + 1)

    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        self.search(prefix)
        return self.startWith

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
