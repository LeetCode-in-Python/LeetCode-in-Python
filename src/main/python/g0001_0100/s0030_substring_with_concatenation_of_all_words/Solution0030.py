# #Hard #String #Hash_Table #Sliding_Window #Top_Interview_150_Sliding_Window
# #2025_09_13_Time_20_ms_(96.85%)_Space_13.11_MB_(74.97%)

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n1 = len(words[0])
        n2 = len(s)
        map1 = {}
        for word in words:
            map1[word] = map1.get(word, 0) + 1
        
        for i in range(n1):
            left = i
            j = i
            c = 0
            map2 = {}
            while j + n1 <= n2:
                word1 = s[j:j + n1]
                j += n1
                if word1 in map1:
                    map2[word1] = map2.get(word1, 0) + 1
                    c += 1
                    while map2[word1] > map1[word1]:
                        word2 = s[left:left + n1]
                        map2[word2] = map2.get(word2, 0) - 1
                        left += n1
                        c -= 1
                    if c == len(words):
                        ans.append(left)
                else:
                    map2.clear()
                    c = 0
                    left = j
        
        return ans
