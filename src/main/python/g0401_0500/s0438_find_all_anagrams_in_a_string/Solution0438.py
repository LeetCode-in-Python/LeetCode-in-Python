# #Medium #Top_100_Liked_Questions #String #Hash_Table #Sliding_Window
# #Algorithm_II_Day_5_Sliding_Window #Programming_Skills_II_Day_12
# #Level_1_Day_12_Sliding_Window/Two_Pointer #Big_O_Time_O(n+m)_Space_O(1)
# #2025_07_25_Time_54_ms_(54.80%)_Space_18.16_MB_(94.43%)

from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map = [0] * 26
        for char in p:
            map[ord(char) - ord('a')] += 1
        
        res = []
        i, j = 0, 0
        
        while i < len(s):
            idx = ord(s[i]) - ord('a')
            # add the new character
            map[idx] -= 1
            # if the length is greater than windows length, pop the left character in the window
            if i >= len(p):
                map[ord(s[j]) - ord('a')] += 1
                j += 1
            
            finish = True
            for k in range(26):
                # if it is not an anagram of string p
                if map[k] != 0:
                    finish = False
                    break
            
            if i >= len(p) - 1 and finish:
                res.append(j)
            
            i += 1
        
        return res
