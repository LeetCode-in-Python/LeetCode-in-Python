# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #String #Hash_Table #Sliding_Window
# #Level_2_Day_14_Sliding_Window/Two_Pointer #Top_Interview_150_Sliding_Window
# #Big_O_Time_O(s.length())_Space_O(1) #2024_06_09_Time_92_ms_(92.59%)_Space_17.1_MB_(93.76%)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        map = [0] * 128
        for char in t:
            map[ord(char) - ord('A')] += 1

        count = len(t)
        begin = 0
        end = 0
        d = float('inf')
        head = 0

        while end < len(s):
            if map[ord(s[end]) - ord('A')] > 0:
                count -= 1
            map[ord(s[end]) - ord('A')] -= 1
            end += 1

            while count == 0:
                if end - begin < d:
                    d = end - begin
                    head = begin
                map[ord(s[begin]) - ord('A')] += 1
                if map[ord(s[begin]) - ord('A')] > 0:
                    count += 1
                begin += 1

        return "" if d == float('inf') else s[head:head + d]
