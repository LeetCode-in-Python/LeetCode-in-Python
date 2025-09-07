# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Dynamic_Programming
# #Backtracking #Big_O_Time_O(N*2^N)_Space_O(2^N*N)
# #2025_07_25_Time_50_ms_(56.82%)_Space_32.70_MB_(87.12%)

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(res, [], s, 0)
        return res

    def backtracking(self, res, curr_arr, s, start):
        if start == len(s):
            res.append(list(curr_arr))
            return
        for end in range(start, len(s)):
            if not self.is_palindrome(s, start, end):
                continue
            curr_arr.append(s[start:end + 1])
            self.backtracking(res, curr_arr, s, end + 1)
            curr_arr.pop()

    def is_palindrome(self, s, start, end):
        while start < end and s[start] == s[end]:
            start += 1
            end -= 1
        return start >= end
