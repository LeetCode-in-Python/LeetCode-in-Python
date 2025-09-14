# #Medium #String #Depth_First_Search #Design #Trie #Top_Interview_150_Trie
# #2025_09_14_Time_1114_ms_(83.50%)_Space_65.69_MB_(47.12%)

class TrieNode:
    def __init__(self):
        self.children = {}    # char -> TrieNode
        self.is_end = False   # end of word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # Word insert karna
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # Word search karna
    def search(self, word: str) -> bool:
        def dfs(node, i):
            # Base case: agar pura word traverse ho gaya
            if i == len(word):
                return node.is_end

            ch = word[i]

            # Case 1: agar char "." hai → sab children explore karo
            if ch == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            # Case 2: normal character
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
