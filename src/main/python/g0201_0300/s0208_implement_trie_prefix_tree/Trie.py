# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Hash_Table #Design #Trie
# #LeetCode_75_Trie #Level_2_Day_16_Design #Udemy_Trie_and_Heap #Top_Interview_150_Trie
# #Big_O_Time_O(word.length())_or_O(prefix.length())_Space_O(N)
# #2025_07_25_Time_44_ms_(68.94%)_Space_32.08_MB_(76.05%)

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWordEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isWordEnd 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
