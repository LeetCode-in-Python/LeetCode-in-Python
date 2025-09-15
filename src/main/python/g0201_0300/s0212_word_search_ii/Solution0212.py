# #Hard #Top_Interview_Questions #Array #String #Matrix #Backtracking #Trie #Top_Interview_150_Trie
# #2025_09_14_Time_615_ms_(82.14%)_Space_27.69_MB_(5.77%)

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        alphabets = [chr(ord("a") + i) for i in range(26)] + ["end"]
        trie = {i:None for i in alphabets}
        for word in words:
            root = trie
            for letter in word:
                if not root[letter]: 
                    root[letter] = {i:None for i in alphabets}
                root = root[letter]
            root["end"] = True

        y, x = len(board), len(board[0])
        visited = [[False]*x for _ in range(y)]
        ans = []

        def remove_word(word, root = trie):
            if word: root[word[0]] = remove_word(word[1:], root[word[0]])

            for i in root:
                if root[i]: return root
                
            return None
        
        def getAns(m, n, root, word):

            if root["end"]: 
                ans.append(word)
                root["end"] = False
                remove_word(word)

            visited[m][n] = True
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                a, b = m+i, n+j
                if 0 <= a < y and 0 <= b < x and visited[a][b] == False and root[board[a][b]]:
                    getAns(a, b, root[board[a][b]], word + board[a][b])
            visited[m][n] = False

            return

        for i in range(y):
            for j in range(x):
                if trie[board[i][j]]:
                    getAns(i, j, trie[board[i][j]], board[i][j])
        
        return ans
