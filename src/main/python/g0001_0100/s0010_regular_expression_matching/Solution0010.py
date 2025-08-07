# #Hard #Top_Interview_Questions #String #Dynamic_Programming #Recursion #Udemy_Dynamic_Programming
# #Big_O_Time_O(m*n)_Space_O(m*n) #2025_07_22_Time_1_ms_(97.40%)_Space_17.83_MB_(64.20%)

class Solution:
    def __init__(self):
        self.cache = None

    def isMatch(self, s: str, p: str) -> bool:
        self.cache = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]
        return self._isMatch(s, p, 0, 0)

    def _isMatch(self, s: str, p: str, i: int, j: int) -> bool:
        if j == len(p):
            return i == len(s)

        if self.cache[i][j] is not None:
            return self.cache[i][j]

        first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        if j + 1 < len(p) and p[j + 1] == '*':
            result = (first_match and self._isMatch(s, p, i + 1, j)) or self._isMatch(s, p, i, j + 2)
        else:
            result = first_match and self._isMatch(s, p, i + 1, j + 1)

        self.cache[i][j] = result
        return result
