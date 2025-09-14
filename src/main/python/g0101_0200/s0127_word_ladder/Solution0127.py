# #Hard #Top_Interview_Questions #String #Hash_Table #Breadth_First_Search
# #Graph_Theory_I_Day_12_Breadth_First_Search #Top_Interview_150_Graph_BFS
# #2025_09_14_Time_21_ms_(99.65%)_Space_18.96_MB_(59.76%)

from typing import List, Set

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        begin_set = set()
        end_set = set()
        word_set = set(wordList)
        visited = set()
        if endWord not in wordList:
            return 0
        length = 1
        str_len = len(beginWord)
        begin_set.add(beginWord)
        end_set.add(endWord)
        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            temp_set = set()
            for s in begin_set:
                chars = list(s)
                for i in range(str_len):
                    old = chars[i]
                    for j in range(ord('a'), ord('z') + 1):
                        chars[i] = chr(j)
                        temp = ''.join(chars)
                        if temp in end_set:
                            return length + 1
                        if temp not in visited and temp in word_set:
                            temp_set.add(temp)
                            visited.add(temp)
                    chars[i] = old
            begin_set = temp_set
            length += 1
        return 0
